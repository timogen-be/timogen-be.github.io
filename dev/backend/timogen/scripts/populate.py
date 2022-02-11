import os, json
import os.path as op
from info_codes import get_codes

JSON_FOLDER = op.join(op.dirname(__file__), "json/")
DATA_FOLDER = op.join(op.dirname(__file__), "../data/")


class PopulateNomenclature:
    """This class is simply used to make a json file that matches the model.
    To use it, we simply create the class then call the `.populate()` method."""

    def __init__(self):
        self.result_file = op.join(DATA_FOLDER, "nomenclature_data.json")
        self.result_content = []  # we fill this little by little
        self.code_dict = get_codes()
        self.nom_id = 0
        self.loc_id = 0
        self.patho_id = 0
        self.line_id = 0

    def populate(self):
        # Base JSON, we will fill it after:
        for json_file in os.listdir(JSON_FOLDER):
            self.add_nomenclature(50)  # 50 stands for kiné, hard coded for now
            content = json.load(open(op.join(JSON_FOLDER, json_file), "r"))
            for location, pathos in content.items():
                self.add_location(location)
                for patho, lines in pathos.items():
                    self.add_patho(patho)
                    for line in lines:
                        self.add_line(line)

        with open(self.result_file, "w+") as outfile:
            json.dump(self.result_content, outfile, indent=4)

    def add_nomenclature(self, activity_id):
        self.nom_id += 1
        self.result_content.append(
            {
                "model": "timogen.nomenclature",
                "pk": self.nom_id,
                "fields": {"activity": activity_id},
            }
        )

    def add_location(self, location):
        self.loc_id += 1

        def prettify(place):
            if "cabinet" in place:
                place = "cabinet du kinésithérapeute, situé %sun hôpital" % (
                    "en dehors d'" if "dehors" in place else "dans "
                )
            elif "handicap" in place:
                place = "personnes handicapées ou résidents"
            elif "personnes âgées" in place:
                place = "personnes âgées"
            elif "domicile" in place:
                place = "domiciles"
            elif "psychiatriques" in place:
                place = "maison de soins psychiatrique"
            elif "hospitalisés" in place:
                place = "hospitalisés"
            elif "centres" in place:
                place = "centres de rééducation fonctionnelle conventionnés"
            elif "ôpital de jour" in place:
                place = "hôpital de jour"
            return place

        self.result_content.append(
            {
                "model": "timogen.location",
                "pk": self.loc_id,
                "fields": {
                    "nomenclature": self.nom_id,
                    "raw": location,
                    "name": prettify(location),
                },
            }
        )

    def add_patho(self, patho):
        if patho.startswith("Indemn"):
            return

        self.patho_id += 1
        breakpoints = []

        def prettify(patho):
            if "iciaires non vis" in patho:
                patho = "Courantes"
                breakpoints = [9, 18]
            elif "§ 11" in patho:
                patho = "Lourdes (§ 11)"
            elif "§ 12" in patho:
                patho = "Soins intensifs / Néonatalogie (§ 12)"
            elif "§ 13" in patho:
                patho = "Périnatalité (§ 13)"
            elif "patients palliatifs" in patho:
                patho = "Patients palliatifs"
            elif "§ 14" in patho:
                patho = "F" + patho[-1] + " (§ 14)"
                breakpoints = [20, 60] if patho[1] == "A" else [60, 80]
            return patho

        self.result_content.append(
            {
                "model": "timogen.patho",
                "pk": self.patho_id,
                "fields": {
                    "location": self.loc_id,
                    "raw": patho,
                    "name": prettify(patho),
                    "breakpoints_encoded": str(breakpoints),
                },
            }
        )

    def add_line(self, line):
        self.line_id += 1
        code = line[1]
        code_info = self.code_dict.get(code)
        is_indemnity = code_info and code_info.description.startswith("Indemn")

        def coma_nbr_to_float(coma_nbr):
            try:
                return eval(coma_nbr.replace(",", "."))
            except:
                return None

        self.result_content.append(
            {
                "model": "timogen.line",
                "pk": self.line_id,
                "fields": {
                    "location": self.loc_id if is_indemnity else None,
                    "patho": self.patho_id if (not is_indemnity) else None,
                    # based on the code info
                    "description": code_info.description if code_info else None,
                    "kind": code_info.code_type if code_info else "STANDARD",
                    "priority": code_info.priority if code_info else None,
                    "duration": code_info.duration if code_info else None,
                    "code": code,
                    "fees": coma_nbr_to_float(line[4]),
                    "bfees_c_p": coma_nbr_to_float(line[5]),
                    "bfees_nc_p": coma_nbr_to_float(line[6]),
                    "bfees_c_np": coma_nbr_to_float(line[7]),
                    "bfees_nc_np": coma_nbr_to_float(line[8]),
                },
            }
        )


if __name__ == "__main__":
    PopulateNomenclature().populate()
