import PyPDF2

pdf_path = r"C:\Users\Admin\Downloads\中国企业出海外派人员选拔与培养体系构建报告.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    with open('extracted_text.txt', 'w', encoding='utf-8') as out_file:
        out_file.write(text)

print("PDF text extracted to extracted_text.txt")