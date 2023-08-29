from pypdf import PdfReader

# =========== Example 1: Ignore header and footer ===========
reader = PdfReader('example.pdf')
page = reader.pages[3]

parts = []

# text, current transformation matrix, text matrix, font dictionary, font size
def visitor_body(text, cm, tm, font_dict, font_size):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)

page.extract_text(visitor_text=visitor_body)
text_body = ''.join(parts)

print(text_body)

#  =========== Example 2: Extract rectangles and texts into a SVG-file ===========
import svgwrite

reader = PdfReader('example.pdf')
page = reader.pages[2]

dwg = svgwrite.Drawing('example.svg', profile='tiny')

def visitor_svg_rect(op, args, cm, tm):
    if op == b're':
        (x, y, w, h) = (args[i].as_numeric() for i in range(4))
        dwg.add(dwg.rect(x, y), (w, h), stroke='red', fill_opacity=0.05)

def visitor_svg_text(text, cm, tm, font_dict, font_size):
    (x, y) = (tm[4], tm[5])
    dwg.add(dwg.text(text, insert=(x, y), fill = 'blue'))

page.extract_text(
    visitor_operand_before=visitor_svg_rect, visitor_text=visitor_svg_text
)
dwg.save()
