import os

from PyPDF2 import PdfMerger


def merge_pdfs(input_folder, output_file):
    merger = PdfMerger()

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            filepath = os.path.join(input_folder, filename)
            merger.append(filepath)

    merger.write(output_file)
    merger.close()


merge_pdfs('input_pdfs', 'merged_output.pdf')
# 此代码仅是展示代码，非实际代码