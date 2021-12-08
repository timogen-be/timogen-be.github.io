import os, json
from bs4 import BeautifulSoup
from requests import request


PROFESSION_CODES = {
    'KINE': 50,
}


class InamiSearchForm:

    BASE_URL = 'https://ondpanon.riziv.fgov.be/SilverPages/fr/Home/SearchByForm'
    BASE_DIR = 'inami_files'


    def __init__(self) -> None:
        os.makedirs(self.BASE_DIR, exist_ok=True)


    def get(self, pro_code, page_offset, page_size):
        return request(
            method='GET',
            url=self.BASE_URL,
            data={
                'Profession': pro_code,
                'PageOffset': page_offset,
                'PageSize': page_size,
            }
        )


    def result_amount(self, pro_code):
        result = self.get(
            pro_code=pro_code,
            page_offset=0,
            page_size=1,
        )
        soup = BeautifulSoup(result.content, 'html.parser')
        for div in soup.find_all('div'):
            if div.get('data-moveto') == '#results-count':
                return int(div.text.split()[0])
        Exception('Not able to find the nomber of results.')


    def request_profession(self, pro_name, pro_code, page_size=1000):

        result_amount = self.result_amount(pro_code)

        for page_offset in range(0, result_amount, page_size):

            # TODO: remove pro_name (from already downloaded files too)
            file_name = f'a{pro_code}_{pro_name}_{page_offset}-{page_offset + page_size}.html'
            file_path = os.path.join(self.BASE_DIR, file_name)

            if not os.path.exists(file_path):

                result = self.get(pro_code, page_offset, page_size)

                with open(file_path, 'w') as file:
                    file.write(result.content.decode('utf-8'))
                    print(result.status_code)


    def request_all_professions(self, page_size=1000):
        for pro_name, pro_code in PROFESSION_CODES.items():
            self.request_profession(pro_name, pro_code, page_size)



PROFESSION_NACECODES = {
    'KINE': '8690501',
}


class BCESearchForm():
    """ DISCLAIMER:
    THIS CLASS DOES NOT WORK, IT CAN BE IMPLEMENTED IN FUTURE VERSIONS BUT IT
    IS LOW PRIORITY.
    """

    BASE_URL = 'https://kbopub.economie.fgov.be/kbopub/zoekactiviteitform.html'
    BASE_REQUEST = '?lang=fr&nacecodes=8690501&keuzeopzloc=gemeenten&gemeente1=&gemeente2=&gemeente3=&gemeente0=&postnummer1=&postnummer2=&postnummer3=&postnummer4=&ondNP=true&_ondNP=on&ondRP=true&_ondRP=on&vest=true&_vest=on&filterEnkelActieve=true&_filterEnkelActieve=on&actionLu=Search'

    def __init__(self) -> None:
        self.post_codes_to_retrieve = set()

    def is_post_code(self, post_code):
        return len(post_code) == 4 and post_code.isdigit()

    def get(self, nacecode, postcode, page_nb):
        return request(
            method='GET',
            url=self.BASE_URL,
            data={
                '_filterEnkelActieve': 'on',
                '_ondNP': 'on',
                '_ondRP': 'on',
                '_vest': 'on',
                'actionLu': 'Search',
                'filterEnkelActieve': 'true',
                'keuzeopzloc': 'gemeenten',
                'lang': 'fr',
                'nacecodes': nacecode, # kiné
                'ondNP': 'true',
                'ondRP': 'true',
                'postnummer1': postcode[0],
                'postnummer2': postcode[0],
                'postnummer3': postcode[0],
                'postnummer4': postcode[0],
                'vest': 'true',
                'page': page_nb,
            }
        )

    def request_profession(self, pro_code):
        with open('therapists_data.json') as f:
            data = json.load(f)
            for therapist in data:
                adress = therapist['fields']['adress']
                post_code = adress.split('\n')[-1].split()[0]
                if self.is_post_code(post_code):
                    self.post_codes_to_retrieve.add(post_code)
        print('post_codes:', sorted(self.post_codes_to_retrieve))

    def request_all_professions(self):
        for _, pro_code in PROFESSION_NACECODES.items():
            self.request_profession(pro_code)


if __name__ == '__main__':
    inami_api = InamiSearchForm()
    inami_api.request_all_professions()
# The following is not functional yet.
    # bce_api = BCESearchForm()
    # bce_api.request_all_professions()
