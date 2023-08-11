from PyPDF2 import PdfWriter
import os

def merge_pdf(filename, file_directory, output_directory):
    """
    Merge PDFs
    """
    merger = PdfWriter()

    if file_directory:
        for pdf in os.listdir(file_directory):
            if pdf.endswith('.pdf'):
                print(pdf)
                # Reference: https://stackoverflow.com/questions/65162124/python3-filenotfounderror-errno-2-no-such-file-or-directory-first-filename
                # os.listdir() returns relative paths, need to reconstruct absolute path to open the files
                pdf_directory = os.path.join(file_directory, pdf)
                merger.append(pdf_directory)

    output_destination = os.path.join(output_directory, filename)
    merger.write(output_destination)
    merger.close()
