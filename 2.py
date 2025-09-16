from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_file, output_folder):
    reader = PdfReader(input_file)

    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        output_file = f"{output_folder}/page_{i + 1}.pdf"
        with open(output_file, 'wb') as out:
            writer.write(out)


split_pdf('input.pdf', 'output_pages')
# 此代码仅是展示代码，非实际代码
