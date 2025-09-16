import os

from pdfminer.high_level import extract_text


def extract_text_from_pdfs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            text = extract_text(input_path)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)


extract_text_from_pdfs('pdf_files', 'text_outputs')
# 此代码仅是展示代码，非实际代码