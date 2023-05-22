import PyPDF2, os, re, json
import os.path as op

PDF_FOLDER = op.join(op.dirname(__file__), "pdfs/")
JSON_FOLDER = op.join(op.dirname(__file__), "json/")
TXT_FOLDER = op.join(op.dirname(__file__), "txt/")


class Tarifs:
    def __init__(self, pdf_path) -> None:
        self.pdf_path = pdf_path
        self.prefix = pdf_path[pdf_path.rfind("/") + 1 : pdf_path.rfind("_") - 1]
        self.txt_path = op.join(TXT_FOLDER, self.prefix + "-%d.txt")
        self.page_total = self.load_txt()
        self.tarifs_dict = self.process_txt()

    def load_txt(self):
        with open(self.pdf_path, "rb") as pdf_bin:
            pdf_reader = PyPDF2.PdfReader(pdf_bin)
            for page_nb, page in enumerate(pdf_reader.pages, 1):
                with open(self.txt_path % page_nb, "w") as output:
                    output.write(page.extract_text())
        return page_nb

    def process_txt(self):
        d = dict()
        for page_nb in range(1, self.page_total):
            title = None
            with open(self.txt_path % page_nb, "r") as f:
                description = None
                content = []
                for line in f.readlines():
                    line = line.strip()
                    if re.search(r"^[A-Z]*\.", line):
                        title = line
                    elif title and content:
                        if content[-1] in ("M =", "= M", "(*)"):
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
                        if line == "M =" or re.search(r"^[0-9]*\,[0-9]*$", line):
                            content.append(line)
                        else:
                            description = line
        with open(op.join(JSON_FOLDER, f"{self.prefix}.json"), "w") as outfile:
            json.dump(d, outfile)
        return d


def load_pdfs(folder):
    for pdf in os.listdir(folder):
        path = op.join(folder, pdf)
        Tarifs(path)


if __name__ == "__main__":
    load_pdfs(PDF_FOLDER)
