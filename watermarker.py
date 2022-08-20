import os
from PyPDF2 import PdfReader, PdfWriter
files = os.listdir('pdfs')
writer = PdfWriter()

for pdf in files:
    reader_base = PdfReader('pdfs/'+pdf)
    for page in reader_base.pages:
        reader_2 = PdfReader('wtr.pdf')
        page_water = reader_2.pages[0]
        page.merge_page(page_water)
        writer.add_page(page)
with open("merged-foo.pdf", "wb") as fp:
    writer.write(fp)