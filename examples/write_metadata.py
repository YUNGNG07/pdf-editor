from datetime import datetime
from pypdf import PdfReader, PdfWriter

filename = 'ISO 32000-2_2020 (PDF 2.0).pdf'
reader = PdfReader(filename)
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add old metadata
metadata = reader.metadata
writer.add_metadata(metadata)

# Format current date and time for metadata
utc_time = '-05"00"'
time = datetime.now().strftime(f'D\072%Y%m%d%H%M%S{utc_time}')

# Add the new metadata
writer.add_metadata(
    {
        '/Author': 'Martin',
        '/Producer': 'Libre Writer',
        '/Title': 'Title',
        '/Subject': 'Subject',
        '/Keywords': 'Keywords',
        '/CreationDate': time,
        'ModDate': time,
        '/Creator': 'Creator',
        '/CustomField': 'CustomField',
    }
)

# Save new PDF to a file
with open('meta-pdf.pdf', 'wb') as f:
    writer.write(f)
