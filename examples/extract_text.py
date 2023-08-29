from pypdf import PdfReader

reader = PdfReader('example.pdf')
page = reader.pages[0]
print(page.extract_text())

# Limit text orientation to extract
# Extract only text oriented up
print(page.extract_text(0))

# Extract text oriented up and turned left
print(page.extract_text((0, 90)))
