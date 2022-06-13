import pdfplumber
from abbrevia import abbreviation

dic = {}


def in_dic(description):
    if description in dic:
        if sign == '-':
            dic[description] -= float(amount)
        else:
            dic[description] += float(amount)
    else:
        dic[description] = float(sign + amount)


with pdfplumber.open("15.03-30.05.pdf") as temp:
    page = 0
    try:
        while temp.pages[page].extract_text():
            first_page = temp.pages[page].extract_text()  # выбираем стр и вытаскиваем текст <class 'str'>
            first_page = first_page.split('\n')  # <class 'list'>
            for i in first_page:
                separated = i.split()
                if separated[0][0].isdigit() and len(separated) > 9:
                    date = separated[0]
                    sign = separated[3]
                    amount = separated[4] if separated[5][-1] != '₽' else separated[4] + separated[5]
                    amount = amount.replace('₽', '').replace(',', '.')
                    description = separated[8:] if not separated[8:][0][0].isdigit() else separated[9:]
                    description = description if description[0] != '₽' else description[1:]
                    description = ' '.join(description)
                    description = abbreviation(description)
                    in_dic(description)
            page += 1
    except IndexError:
        pass
# print(dic)

# ---------------------Запись в файл--------------------------#

from openpyxl.writer.excel import save_workbook
from openpyxl import *

FILE_NAME = 'excel.xlsx'

try:
    wb = load_workbook(FILE_NAME)
except:
    wb = Workbook()

ws = wb.create_sheet('new')

num = 2
_cell = ws['A1']
_cell2 = ws['B1']

_cell.value = 'Описание'
_cell2.value = 'Сумма'

for descr, sum in dic.items():
    _cell = ws['A' + str(num)]  # Определяем необходимую ячейку на листе
    _cell2 = ws['B' + str(num)]

    _cell.value = descr  # Пишем в ячейке
    _cell2.value = sum
    num += 1
    print(descr, '->', sum)

save_workbook(wb, FILE_NAME)
