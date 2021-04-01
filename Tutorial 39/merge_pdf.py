# pip install PyPDF2
from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()
for item in os.listdir():
    if item.endswith(".pdf"):
        merger.append(item)
merger.write("hello_world.pdf")
merger.close()