import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import os.path


URL_CODES_KINE = 'https://ondpanon.riziv.fgov.be/Nomen/fr/search/by-article-tree?articleId=2669&onlyActiveCodes=True'
FILENAME_CODES_KINE = os.path.join(os.path.dirname(__file__), 'html/codes_kine.html')

if not os.path.exists(FILENAME_CODES_KINE):  # should add: or too old
    response = requests.get(URL_CODES_KINE)
    if response.status_code == 200:
        with open(FILENAME_CODES_KINE, 'w+') as f:
            f.write(response.content)
    else:
        exit('Failed download ')

with open(FILENAME_CODES_KINE, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')


codes_explanation = {s.string: s.get('value') for s in soup.find_all('option')}

code_types = 'INTAKE REPORT CONSULT DOUBLE SECOND MLD STANDARD'.split()
"""
INTAKE: first seance.
REPORT: written report.
CONSULT: seance with no doctor's agreement.
DOUBLE: 1 seance separated in 2.
SECOND: 2nd time of the day.
MLD: manual lymphatic drainage.
STANDARD: others.
"""

@dataclass
class Code:
    code_type: str
    duration: int
    priority: int  # 0, 1, 2, 3: 0 is max


def is_code(s):
    return s.isdigit() and len(s) == 6

def get_codes():
    codes = dict()
    for k, v in codes_explanation.items():

        v = v.replace(',', '')
        pos = v.find('minutes') + 1

        code_type = 'STANDARD'
        duration = int(v[pos-5:].split()[0]) if pos else 0
        priority = 0

        if 'deux périodes' in v:
            code_type = 'DOUBLE'
        elif 'journée' in v:
            code_type = 'SECOND'
        elif v.startswith('Rapport écrit'):
            code_type = 'SECOND'
        elif v.startswith('Intake'):
            code_type = 'INTAKE'
        elif v.endswith('consultatif'):
            code_type = 'CONSULT'
        elif 'drainage lymphatique manuel' in v:
            code_type = 'MLD'
        elif 'la séance' in v:
            priority = 1
        elif 'les séances' in v:
            priority = len([i for i in v.split() if is_code(i)])
        else:
            # this is the default case
            pass 
        codes[k] = Code(code_type, duration, priority)
    return codes


if __name__ == '__main__':
    codes = get_codes()
    print(*codes.items(), sep='\n')
