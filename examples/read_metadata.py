from pypdf import PdfReader

filename = 'ISO 32000-2_2020 (PDF 2.0).pdf'

reader = PdfReader(filename)
meta = reader.metadata
# 1003
print(len(reader.pages))

# ISO
print(meta.author)
# Adobe Acrobat Pro DC 18.11.20035
print(meta.creator)
# Adobe Acrobat Pro DC 18.11.20035
print(meta.producer)
# None
print(meta.subject)
# ISO 32000-2:2020 with errata
print(meta.title)
