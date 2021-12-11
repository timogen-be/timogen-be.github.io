import PyPDF2, os, re, json

DEBUG_MODE = True
PDF_FOLDER = 'pdfs/'


class Tarifs:
    def __init__(self, pdf_path) -> None:
        self.pdf_path = pdf_path
        self.prefix = pdf_path[pdf_path.rfind('/')+1:pdf_path.rfind('_')-1]
        self.txt_path = f'txt/{self.prefix}-%d.txt'
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
        with open("tarifs.json", "w") as outfile: 
            json.dump(d, outfile, )
        return d


def load_pdfs(folder):
    for pdf in os.listdir(folder):
        path = os.path.join(folder, pdf)
        Tarifs(path)


if __name__ == '__main__':
    load_pdfs(PDF_FOLDER)
