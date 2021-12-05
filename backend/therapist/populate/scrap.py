import os
from bs4 import BeautifulSoup
from requests import request


PROFESSION_CODES = {
    'Kine': 50,
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

            file_name = f'{pro_name}_{page_offset}-{page_offset + page_size}.html'
            file_path = os.path.join(self.BASE_DIR, file_name)

            if not os.path.exists(file_path):

                result = self.get(pro_code, page_offset, page_size)

                with open(file_path, 'w') as file:
                    file.write(result.content.decode('utf-8'))
                    print(result.status_code)


    def request_all_professions(self, page_size=1000):
        for pro_name, pro_code in PROFESSION_CODES.items():
            self.request_profession(pro_name, pro_code, page_size)


if __name__ == '__main__':
    api = InamiSearchForm()
    api.request_all_professions()
