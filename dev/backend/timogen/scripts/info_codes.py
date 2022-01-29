import requests
from enum import Enum
from bs4 import BeautifulSoup
from dataclasses import dataclass
import os.path as op

URL_CODES_KINE = "https://ondpanon.riziv.fgov.be/Nomen/fr/search/by-article-tree?articleId=2669&onlyActiveCodes=True"
URL_CODES_OTHERS = "https://ondpanon.riziv.fgov.be/Nomen/fr/search/by-article-tree?articleId=5363&onlyActiveCodes=False"
FILENAME_CODES_KINE = op.join(op.dirname(__file__), "html/codes_kine.html")
FILENAME_CODES_OTHERS = op.join(op.dirname(__file__), "html/codes_others.html")


def retrieve_documents(filename, url):
    if not op.exists(filename):  # should add: or too old
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb+") as f:
                f.write(response.content)
        else:
            exit("Failed download ")

    with open(filename, "r") as f:
        soup = BeautifulSoup(f, "html.parser")
    return soup


soup = retrieve_documents(FILENAME_CODES_KINE, URL_CODES_KINE)
codes_explanation = {s.string: s.get("value") for s in soup.find_all("option")}

soup = retrieve_documents(FILENAME_CODES_OTHERS, URL_CODES_OTHERS)
codes_explanation |= {s.string: s.get("value") for s in soup.find_all("option")}

CODE_KIND_CHOICES = [
    ("INTAKE", "Intake"),
    ("REPORT", "Report"),
    ("CONSULT", "Consultative"),
    ("DOUBLE", "Double"),
    ("SECOND", "Second"),
    ("MLD", "Manual Lymphatic Drainage"),
    ("STANDARD", "Others"),
]


@dataclass
class Code:
    code_type: str
    duration: int
    priority: int  # 0, 1, 2, 3: 0 is max
    description: str


def is_code(s):
    return s.isdigit() and len(s) == 6


def get_codes():
    codes = dict()
    for k, v in codes_explanation.items():

        v = v.replace(",", "")
        pos = v.find("minutes") + 1

        code_type = "STANDARD"
        duration = int(v[pos - 5 :].split()[0]) if pos else 0
        priority = 0

        if "deux périodes" in v:
            code_type = "DOUBLE"
        elif 'e séance de' in v:
            code_type = "SECOND"
        elif "journée" in v:
            code_type = "STANDARD"
        elif v.startswith("Rapport écrit"):
            code_type = "REPORT"
        elif v.startswith("Intake"):
            code_type = "INTAKE"
        elif v.endswith("consultatif"):
            code_type = "CONSULT"
        elif "drainage lymphatique manuel" in v:
            code_type = "MLD"
        elif "Indemnité" in v:
            code_type = " ".join(v.split()[-2:])
        elif "la séance" in v:
            priority = 1
        elif "les séances" in v:
            priority = len(
                [i for i in v.split() if is_code(i) and i[0] != 6]
            )  # 6 is the start for MLD
        codes[k] = Code(code_type, duration, priority, description=v)
    return codes


if __name__ == "__main__":
    codes = get_codes()
    print(*codes.items(), sep="\n")
