from pypdf import PdfReader, PdfWriter, PdfMerger
from tkinter import ttk
import os
import tkinter as tk

def read_metadata(file, data='author'):
    path = file.replace('\\', '/')
    reader = PdfReader(path)
    meta = reader.metadata

    if data == 'pages':
        num = len(reader.pages)
        print(f'The number of pages in this PDF documents is: {num}')
        return num
    elif data == 'author':
        author = meta.author
        print(f'The author is: {author}')
        return author
    elif data == 'creator':
        creator = meta.creator
        print(f'The creator is: {creator}')
        return creator
    elif data == 'producer':
        producer = meta.producer
        print(f'The producer is: {producer}')
        return producer
    elif data == 'subject':
        subject = meta.subject
        print(f'The subject is: {subject}')
        return subject
    elif data == 'title':
        title = meta.title()
        print(f'The title is: {title}')
        return title

def read_pdf(file, page_num=0, orientation=0):
    reader = PdfReader(file)

    page = reader.pages[page_num]
    return page.extract_text(orientation)

def extract_attach(file):
    reader = PdfReader(file)

    for name, content_list in reader.attachments:
        for i, content in enumerate(content_list):
            with open(f'{name}{i}', 'wb') as fp:
                fp.write(content)

def encrypt_pdf(file):
    files = file.split('\\')
    directory = '/'.join([str(item) for item in files[:(len(files)-1)]])
    reader = PdfReader(file)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add password
    writer.encrypt('password', algorithm='AES-256')

    # Save new PDF to a file
    with open(os.path.join(directory, 'pdf_crypted.pdf'), 'wb') as f:
        writer.write(f)

def decrypt_pdf(file):
    files = file.split('\\')
    directory = '/'.join([str(item) for item in files[:(len(files)-1)]])
    reader = PdfReader(file)
    writer = PdfWriter()

    if reader.is_encrypted():
        reader.decrypt('password')

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Save new PDF to a file
    with open(os.path.join(directory, 'pdf_decrypted.pdf'), 'wb') as f:
        writer.write(f)

def rotate_pdf(file, page_num=0, angle=90):
    files = file.split('\\')
    directory = '/'.join([str(item) for item in files[:(len(files)-1)]])
    reader = PdfReader(file)
    writer = PdfWriter()

    writer.add_page(reader.pages[page_num])
    writer.pages[page_num].rotate(angle)

    with open(os.path.join(directory, 'pdf_rotated.pdf'), 'wb') as f:
        writer.write(f)

def merge_pdf(file_directory):
    merger = PdfMerger()

    files = [f for f in os.listdir(file_directory) if f.endswith('.pdf')]

    for pdf in files:
        # Need to construct complete path to find the PDF files
        # Reference: https://stackoverflow.com/questions/65162124/python3-filenotfounderror-errno-2-no-such-file-or-directory-first-filename
        docs = os.path.join(file_directory, pdf)
        merger.append(docs)

    with open(os.path.join(file_directory, 'pdf_merger.pdf'), 'wb') as append:
        merger.write(append)

root = tk.Tk()
root.title('PDF Merger')
root.geometry('1250x720')

if __name__ == '__main__':
    directory = r'C:\Users\yungng07\Documents\pdf-editor\files'
    file = r'C:\Users\yungng07\Documents\pdf-editor\files\pdf_sample3.pdf'

    # merge_pdf(directory)
    # read_metadata(file)
    # print(read_pdf(file, orientation=(90)))
    encrypt_pdf(file)
