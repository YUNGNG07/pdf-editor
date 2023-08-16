from PyPDF2 import PdfMerger
import os

merger = PdfMerger()
file_directory = r'C:/Users/yungng07/Documents/PDF-Editor/'

files = [f for f in os.listdir(file_directory) if f.endswith('.pdf')]

for pdf in files:
    merger.append(pdf)

with open(os.path.join(file_directory, 'python_cheatsheets.pdf'), 'wb') as append:
    merger.write(append)
