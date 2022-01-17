# pip install PyPDF2
from PyPDF2 import PdfFileMerger
import os
x = []
merger = PdfFileMerger()
for item in os.listdir():
    if item.endswith(".pdf"):
        x.append(item)
print(x)
x.sort()
print(x)
for i in range(len(x)):
    merger.append(x[i])
merger.write("hello_world.pdf")
merger.close()