import os
from PyPDF2 import PdfReader, PdfMerger
merger = PdfMerger()
with open('pdfs/twopage.pdf', 'rb') as pdf1:
    reader = PdfReader(pdf1)
    page = reader.pages[0]
    text = page.extract_text()
    print(text)
files = os.listdir('pdfs')
print(files)
for pdf in files:
    print(pdf)
    merger.append('pdfs/'+pdf)

merger.write("merged-pdf.pdf")
merger.close()
