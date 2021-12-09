import PyPDF2, os

PDF_FOLDER = 'pdfs/'
TXT_FOLDER = 'txt/'


class Tarifs:
    def load(self, pdf_name):
        with open(pdf_name, 'rb') as f:
            pdf_stream = PyPDF2.PdfFileReader(f)
            for page_nb in range(pdf_stream.getNumPages()):
                page = pdf_stream.getPage(page_nb)
                new_name = pdf_name[:pdf_name.rfind('_')-1]
                with open(f"{new_name}-{page_nb}.txt", 'w') as output:
                    output.write(page.extractText())

    def load_pdfs(self, folder):
        for pdf in os.listdir(folder):
            path = os.path.join(folder, pdf)
            self.load(path)

    def read(self):
        with open('tarifs/tarif_%d.txt' % page_nb, 'f') as f:
            for line in input.readlines():
                if line[:1] == ' ':
                    print()
                print(line, end=' ')


if __name__ == '__main__':
    tarifs = Tarifs()
    tarifs.load_pdfs(PDF_FOLDER)
