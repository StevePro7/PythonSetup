# 10. Automate PDF Manipulation
from  PyPDF2 import PdfMerger


def merge_pdf(pdf_list, output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
