import pdfplumber
import re

dic = {}
page = 0
plus = 0
minus = 0

from abbrevia import abbreviation

with pdfplumber.open("15.03-30.05.pdf") as temp:
    try:
        while temp.pages[page].extract_text():
            first_page = temp.pages[page].extract_text()  # выбираем стр и вытаскиваем текст
            period = re.findall(r'период.+', first_page,)
            page += 1
            sum = re.findall(r'[₽].{0,}[₽]', first_page)  # сумма
            description = re.findall(r'[₽]\s\w.{0,}', first_page)  # описание
            # print(first_page)
            for i in range(len(description)):
                description_each = description[i][2:]  # убираем ₽
                # print(description_each)
                sign = sum[i][2:3]  # знак
                # print(sign)
                number = float(sum[i][4:].replace(',', '.').replace(' ', '').replace('₽', ''))  # цифра
                if sign == '-':
                    minus -= number
                else:
                    plus += number
                # print(description_each)
                description_each = abbreviation(description_each)
                # print(description_each)
                if description_each not in dic and sign == '-':
                    dic[description_each] = float('-' + str(number))
                elif description_each not in dic and sign == '+':
                    dic[description_each] = number
                elif description_each in dic and sign == '-':
                    dic[description_each] -= number
                elif description_each in dic and sign == '+':
                    dic[description_each] += number
    except IndexError:
        pass

print(period)
# for i in dic:
#     print(i, dic[i])

# ---------------------Запись в файл--------------------------#

# from openpyxl.writer.excel import save_workbook
# from openpyxl import *
#
# FILE_NAME = 'excel.xlsx'
#
# try:
#     wb = load_workbook(FILE_NAME)
# except:
#     wb = Workbook()
#
# ws = wb.create_sheet('Students')
#
# num = 2
# _cell = ws['A1']
# _cell2 = ws['B1']
#
# _cell.value = 'Описание'
# _cell2.value = 'Сумма'
#
#
#
# for descr, sum in dic.items():
#
#     _cell = ws['A' + str(num)]  # Определяем необходимую ячейку на листе
#     _cell2 = ws['B' + str(num)]
#
#     _cell.value = descr  # Пишем в ячейке
#     _cell2.value = sum
#     num += 1
#     print(descr, '->', sum)
#
# # Сохраняем документ
# save_workbook(wb, FILE_NAME)
