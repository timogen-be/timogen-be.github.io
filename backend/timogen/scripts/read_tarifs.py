import PyPDF2, os, re, json

DEBUG_MODE = True
PDF_FOLDER = os.path.join(os.path.dirname(__file__), 'pdfs/')
JSON_FOLDER = os.path.join(os.path.dirname(__file__), '../json/')
TXT_FOLDER = os.path.join(os.path.dirname(__file__), 'txt/')

class Tarifs:
    def __init__(self, pdf_path) -> None:
        self.pdf_path = pdf_path
        self.prefix = pdf_path[pdf_path.rfind('/')+1:pdf_path.rfind('_')-1]
        self.txt_path = os.path.join(TXT_FOLDER, f'/{self.prefix}-%d.txt')
        self.page_total = self.load_txt()
        self.tarifs_dict = self.process_txt()
        if DEBUG_MODE:
            self.show_tarifs()

    def show_tarifs(self):
        for key, values in self.tarifs_dict.items():
            print(key)
            for k, vs in values.items():
                print(' ', k)
                for v in vs:
                    print(' '*3, v)

    def load_txt(self):
        with open(self.pdf_path, 'rb') as pdf_bin:
            pdf_stream = PyPDF2.PdfFileReader(pdf_bin)
            page_total = pdf_stream.getNumPages()
            for page_nb in range(page_total):
                page = pdf_stream.getPage(page_nb)
                with open(self.txt_path % page_nb, 'w') as output:
                    output.write(page.extractText())
        return page_total

    def process_txt(self):
        d = dict()
        for page_nb in range(1, self.page_total):
            title = None
            with open(self.txt_path % page_nb, 'r') as f:
                description = None
                content = []
                for line in f.readlines():
                    line = line.strip()
                    if re.search(r'^[A-Z]*\.', line):
                        title = line
                    elif title and content:
                        if content[-1] in ('M =', '= M', '(*)'):
                            content[-1] = line
                        else:
                            content.append(line)
                        if len(content) == 9:
                            if title not in d:
                                d[title] = dict()
                            if description not in d[title]:
                                d[title][description] = []
                            d[title][description].append(list(content))
                            content = []
                    else:
                        if line == 'M =' or re.search(r'^[0-9]*\,[0-9]*$', line):
                            content.append(line)
                        else:
                            description = line
        d = self.prettify(d)
        with open(os.path.join(JSON_FOLDER, f"{self.prefix}.json"), "w") as outfile:
            json.dump(d, outfile)
        return d

    def prettify(self, d):
        new_d = {}
        for place, pathos in d.items():
            if 'cabinet' in place:
                new_place = 'cabinet du kinésithérapeute, situé %sun hôpital' % 'en dehors d\'' if 'dehors' in place else 'dans'
            elif 'handicap' in place:
                new_place = 'personnes handicapées ou résidents'
            elif 'personnes âgées' in place:
                new_place = 'personnes âgées'
            elif 'domicile' in place:
                new_place = 'domiciles'
            elif 'psychiatriques' in place:
                new_place = 'maison de soins psychiatrique'
            elif 'hospitalisés' in place:
                new_place = 'hospitalisés'
            elif 'centres' in place:
                new_place = 'centres de rééducation fonctionnelle conventionnés'
            elif 'ôpital de jour' in place:
                new_place = 'hôpital de jour'
            else:
                new_place = place
            # pathos
            new_pathos = {}
            for patho, lsts in pathos.items():
                if 'iciaires non vis' in patho:
                    new_patho = 'Courantes'
                elif '§ 11' in patho:
                    new_patho = 'Lourdes (§ 11)'
                elif '§ 12' in patho:
                    new_patho = 'Soins intensifs / Néonatalogie (§ 12)'
                elif '§ 13' in patho:
                    new_patho = 'Périnatalité (§ 13)'
                elif 'patients palliatifs' in patho:
                    new_patho = 'Patients palliatifs'
                elif '§ 14' in patho:
                    new_patho = 'F' + patho[-1] + ' (§ 14)'
                else:
                    new_patho = patho
                new_pathos[new_patho] = lsts
            new_d[new_place] = new_pathos
        return new_d

def load_pdfs(folder):
    for pdf in os.listdir(folder):
        path = os.path.join(folder, pdf)
        Tarifs(path)


if __name__ == '__main__':
    load_pdfs(PDF_FOLDER)
