from docx import Document
from docx.shared import Cm, Pt

from config import desktop


#  90 символов x 73 строки
def create_pages_to_print(txt):
    txt = txt.split('\n')

    lines = []
    for line, string in enumerate(txt):
        lines.append([])
        for i in range(0, len(string), 90):
            lines[-1].append(string[i: i + 90])

    pages = ['' for _ in range(len(lines[0]))]
    for g in range(len(lines)):
        for i, string in enumerate(lines[g]):
            pages[i] += string
    return pages


def create_docx(txt, name):
    pages = create_pages_to_print(txt)

    doc = Document()
    style = doc.styles['Normal']

    style.font.name = 'Lucida Console'
    style.font.size = Pt(10)

    section = doc.sections[0]
    section.left_margin = Cm(1.3)
    section.right_margin = Cm(1.2)
    section.top_margin = Cm(0.75)
    section.bottom_margin = Cm(0.75)

    for i in range(len(pages)):
        doc.add_paragraph(pages[i])
        doc.add_page_break()
    while True:
        try:
            doc.save(f'{desktop}\\{name}.docx')
            break
        except:
            print(f'Для новой записи закройте файл {name}.docx')
            input('Как будет готово, нажмите Enter')
            continue
