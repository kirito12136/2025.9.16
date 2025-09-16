import os

import pytesseract
from pdf2image import convert_from_path


def ocr_pdfs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            images = convert_from_path(input_path)

            text = ""
            for image in images:
                text += pytesseract.image_to_string(image) + "\n"

            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)


ocr_pdfs('scanned_pdfs', 'ocr_outputs')
# 此代码仅是展示代码，非实际代码
