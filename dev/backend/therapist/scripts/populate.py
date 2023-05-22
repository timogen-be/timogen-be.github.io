import os
from bs4 import BeautifulSoup
import json

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "../data/")


class InamiHTML:

    TARGET_CLASS = "card"

    def __init__(self, path) -> None:
        self.soup = self.get_soup(path)
        self.html_therapists = self.get_html_therapists()

    def get_soup(self, path):
        with open(path) as fp:
            return BeautifulSoup(fp, "html.parser")

    def format_address(self, raw_address):
        if raw_address in ["Pas d’adresse de travail principale connue", 'Geen hoofdwerkadres gekend']:
            return ""
        return "\n".join(
            [
                " ".join(elem.strip() for elem in line.split() if elem.strip())
                for line in raw_address.split("\n")
                if line.strip()
            ][-2:]
        ).title()

    def is_html_therapist(self, tag):
        return self.TARGET_CLASS in tag.get("class", [])

    def get_html_therapists(self):
        return self.soup.find_all(self.is_html_therapist)

    def add_to_data_list(self, data_list, activity):
        for therapist in self.html_therapists:
            data = {
                l.text.strip(): l.parent.div.text.strip()
                for l in therapist.find_all("label")
            }
            therapist = dict()
            therapist["model"] = "therapist.therapist"
            therapist["pk"] = len(data_list) + 1
            inami_start = data["RIZIV-nr"]
            therapist["fields"] = {
                "activity": activity,
                "inami_nb": f"{inami_start[0]}-{inami_start[1:]}-{data['Kwalificatie'].split()[0]}",
                "name": data["Naam"].title(),
                "address": self.format_address(data["Werkadres"]),
                "contracted": bool(data["Conv."] == "Geconventioneerd"),
            }
            data_list.append(therapist)


class InamiFiles:

    BASE_DIR = "inami_files"

    def __init__(self) -> None:
        self.data_list = []

    def get_paths(self):
        return [
            os.path.join(self.BASE_DIR, filename)
            for filename in os.listdir(self.BASE_DIR)
        ]

    def data_to_json(self):
        for path in self.get_paths():
            html = InamiHTML(path)
            activity = int(path.split("/")[-1].split("_")[0][1:])
            html.add_to_data_list(self.data_list, activity)
            print(path)
        with open(os.path.join(DATA_FOLDER, "therapists_data.json"), "w+") as f:
            json.dump(self.data_list, f, indent=4)


if __name__ == "__main__":
    res = InamiFiles()
    res.data_to_json()
    # then use ./manage.py loaddata therapist/data/therapists_data.json
