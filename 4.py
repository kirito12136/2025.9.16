from PyPDF2 import PdfReader, PdfWriter


def add_watermark(input_pdf, watermark_pdf, output_pdf):
    watermark = PdfReader(watermark_pdf)
    watermark_page = watermark.pages[0]

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf, 'wb') as out:
        writer.write(out)
    # 此代码仅是展示代码，非实际代码