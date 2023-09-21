from pypdf import PdfMerger
from tkinter import ttk
import os
import tkinter as tk

def merge_pdf():
    merger = PdfMerger()
    file_directory = r'C:/Users/yungng07/Documents/pdf-editor/'

    files = [f for f in os.listdir(file_directory) if f.endswith('.pdf')]

    for pdf in files:
        merger.append(pdf)

    with open(os.path.join(file_directory, 'pdf_merger.pdf'), 'wb') as append:
        merger.write(append)

root = tk.Tk()
root.title('PDF Merger')
root.geometry('1250x720')

