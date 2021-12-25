import json
from collections import OrderedDict
from scripts.info_codes import get_codes


class NomenclatureLine:

    codes_info = get_codes()

    structure = [
        ('HOURLY_RATE', slice(0, 1), float),
        ('CODE', slice(1, 3), str),  # AMB, HOS
        ('DURATION', slice(3, 4), float),
        ('FEES', slice(4, 5), float),
        ('BACK_FEES', slice(5, 9), float),  # PREF-CONV, PREF-NC, NP-CONV, NP-NC
    ]

    def __init__(self, lst:list) -> None:
        self.content = {
            title: [
                self.safe_eval(value.replace(',', '.'), _type) for value in lst[_slice]
                ] for (title, _slice, _type) in self.structure
        }
        code_info = self.codes_info.get(self.get_code(0)) or self.codes_info.get(self.get_code(1))
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

    def get_code(self, hos:bool=False):
        return self.content['CODE'][hos]

    def get_back_fees(self, nc:bool=False, np:bool=False):
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
                pathos[patho] = [NomenclatureLine(line) for line in pathos[patho]]
                print(pathos[patho])

    def get_places(self):
        return self.content

    def get_pathos(self, place):
        return self.content.get(place)

    def get_all_lines(self, place, patho):
        return self.content[place][patho]

    def get_time_lines(self, place, patho, time):
        return list(filter(lambda line: line.get_duration() == time, self.get_all_lines(place, patho)))

    def get_times(self, place, patho):
        return sorted(set([line.get_duration() for line in self.content[place][patho]]))

    def get_codes_and_prices(self, place, patho, amb, contracted, preferential, seance_id, duration=24, consultative=False):
        """return value: [(code, price)], success:bool"""
        lines = self.get_all_lines(place, patho)
        duration_lines = [line for line in lines if line.get_duration() == duration]
        if not duration_lines:
            return lines, False
        result = []

        # Courantes : seance 1-9, 10-18, 18-...
        if patho.startswith('Courantes'):
            if seance_id < 10 or len(duration_lines) <= 2:
                first_line = duration_lines[0]
            elif seance_id < 19 or len(duration_lines) <= 3:
                first_line = duration_lines[1]
            else:
                first_line = duration_lines[2]
 
        # Courantes : seance 1-20, 21-60, 60-...
        if patho.startswith('FA'):
            if seance_id < 21 or len(duration_lines) <= 2:
                first_line = duration_lines[0]
            elif seance_id < 61 or len(duration_lines) <= 3:
                first_line = duration_lines[1]
            else:
                first_line = duration_lines[2]

        if consultative:
            first_line = duration_lines[-1]



if __name__ == '__main__':
    nom_kine = Nomenclature('json/tarif_kinesitherapeute.json')
    for place in nom_kine.get_places():
        for patho in nom_kine.get_pathos(place):
            print(patho)
            for time in nom_kine.get_times(place, patho):
                print(time, len(nom_kine.get_time_lines(place, patho, time)))

    # print(nom_kine.get_places())
    # print(nom_kine.get_pathos(0))
