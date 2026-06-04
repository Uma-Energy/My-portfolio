from pathlib import Path
from pypdf import PdfReader

path = Path(r'C:/Users/DELL/Documents/My Documents/VIKTHORE WEB PAGE/VICTOR IKECHUKWU PORTFOLIO_files/My_CV.txt..pdf')
reader = PdfReader(str(path))
for i, page in enumerate(reader.pages, 1):
    print('--- PAGE', i, '---')
    text = page.extract_text()
    if text:
        print(text)
    else:
        print('[NO TEXT EXTRACTED]')
