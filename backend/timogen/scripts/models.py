import json
from collections import OrderedDict
from timogen.scripts.info_codes import get_codes


class NomenclatureLine:

    codes_info = get_codes()

    structure = [
        ('HOURLY_RATE', slice(0, 1), float),
        ('CODE', slice(1, 3), str),  # AMB, HOS
        ('DURATION', slice(3, 4), float),
        ('FEES', slice(4, 5), float),
        (
            'BACK_FEES', slice(5, 9), float
        ),  # PREF-CONV, PREF-NC, NP-CONV, NP-NC  -> on 01/01/2022 becomes PREF, NP
    ]

    def __init__(self, lst: list) -> None:
        self.content = {
            title: [
                self.safe_eval(value.replace(',', '.'), _type)
                for value in lst[_slice]
            ]
            for (title, _slice, _type) in self.structure
        }
        code_info = self.codes_info.get(
            self.get_code(0)) or self.codes_info.get(self.get_code(1))
        # overwrite with our codes info
        if code_info:
            self.content['CODE_TYPE'] = [code_info.code_type]
            self.content['DURATION'] = [code_info.duration]
            self.content['PRIORITY'] = [code_info.priority]

    def __repr__(self):
        return str(self.content)

    def __getattr__(self, name):
        """defines get_hourly_rate, get_duration, get_fees all at once."""
        if name.startswith('get_'):
            return lambda: self.content[name[4:].upper()][0]

    def get_code(self, hos: bool = False):
        return self.content['CODE'][hos]

    def get_back_fees(self, nc: bool = False, np: bool = False):
        return self.content['BACK_FEES'][np * 2 + nc]

    def safe_eval(self, value, converter):
        try:
            return converter(value.replace(',', '.'))
        except:
            return None


class Nomenclature:

    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as f:
            self.content = json.load(f, object_pairs_hook=OrderedDict)
        for pathos in self.content.values():
            for patho in pathos:
                pathos[patho] = [
                    NomenclatureLine(line) for line in pathos[patho]
                ]

    def render_json(self):
        return json.dumps(self, default=lambda obj: obj.content)

    def debug(self, level=3):
        """ 3 levels of debug:
        1:places
        2:pathos
        3:nomenclature_lists
        """
        for place, pathos in self.get_places().items():
            print(place)
            if level <= 1:
                continue
            for patho, lsts in pathos.items():
                print('', patho)
                if level <= 2:
                    continue
                for lst in lsts:
                    print('  ', lst)

    def get_places(self):
        """returns a dict with all."""
        return self.content

    def get_pathos(self, place):
        """returns a dict about a place."""
        return self.content.get(place)

    def get_all_lines(self, place, patho):
        return self.content[place][patho]

    def get_time_lines(self, place, patho, time):
        return list(
            filter(lambda line: line.get_duration() == time,
                   self.get_all_lines(place, patho)))

    def get_times(self, place, patho):
        return sorted(
            set([line.get_duration() for line in self.content[place][patho]]))

    def get_indemnities(self, patho):
        indemnities = self.get_all_lines(
            'domiciles',
            'Indemnité pour les frais de déplacement du kinésithérapeute')
        # list of (patho_contains, code_contains) -> need to be ordered so no dict
        indemnity_types = [
            ('FA', 'Fa'),
            ('FB', 'Fb'),
            ('palliatif', 'palliatif'),
            ('Lourdes', 'lourde'),
            ('', 'autres'),  # will always be contained
        ]
        for pc, cc in indemnity_types:
            if pc in patho:
                return list(
                    filter(lambda line: cc in line.get_code_type(),
                           indemnities))[0]

    def get_priority(self, patho, seance_id):
        """lowest priority for the first seances."""
        seance_breakpoints = [
            ('Courantes', (9, 18)),  # Courantes : seance 1-9, 10-18, 18-...
            ('FA', (20, 60)),  # FA : seance 1-20, 21-60, 61-...
            ('FB', (60, 80)),  # FA : seance 1-60, 61-80, 81-...
        ]
        for name, bps in seance_breakpoints:
            if patho.startswith(name):
                return 0 if seance_id <= bps[
                    0] else 1 if seance_id <= bps[1] else 2
        return 0

    def get_corresp_lines(self,
                          place,
                          patho,
                          seance_id,
                          duration=30,
                          consultative=False):
        """return value: [(code, price)], success:bool"""
        result = []
        all_lines = self.get_all_lines(place, patho)

        # DURATION
        lines = list(
            filter(lambda line: line.get_duration() == duration, all_lines))

        # DOM
        if place == 'domiciles':
            result.append(self.get_indemnities(patho))

        # CONSULT
        if consultative:
            return result + list(
                filter(lambda line: line.get_code_type() == 'CONSULT',
                       lines))[:1]

        # INTAKE
        if seance_id == 1:
            result += list(
                filter(lambda line: line.get_code_type() == 'INTAKE',
                       all_lines))[:1]
            print('result:', result)

        # Get the highest corresponding priority
        for p in range(self.get_priority(patho, seance_id), -1, -1):
            try:
                result += list(
                    filter(lambda line: line.get_priority() == p, lines))[:1]
                break
            except:
                pass

        return result


if __name__ == '__main__':
    nom_kine = Nomenclature('json/tarif_kinesitherapeute.json')

    nom_kine.debug(level=2)
"""
    place = next(iter(nom_kine.get_places().keys()))  # Get first item
    print('place:', place)

    patho = next(iter(nom_kine.get_pathos(place).keys()))
    print('patho:', patho)

    line = nom_kine.get_corresp_lines(
        place=place,
        patho=patho,
        seance_id=1
    )
    print('lines:', *line, sep='\n')
"""
