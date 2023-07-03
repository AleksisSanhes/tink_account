import pdfplumber
import re
from abbrevia import abbreviation
from datetime import date  # для сравнения дат

dic = {}
input_date = "01.04.2022".split('.')
input_date = date(int(input_date[2]), int(input_date[1]), int(input_date[0]))


def check_date(current_date):  # проверяет, чтоб дата введеная была равна, либо меньше, даты на странице
    current_date = date(int(current_date[2]), int(current_date[1]), int(current_date[0]))
    return input_date <= current_date


def check_in_dic(description_each):
    if description_each not in dic and sign == '-':
        dic[description_each] = float('-' + str(number))
    elif description_each not in dic and sign == '+':
        dic[description_each] = number
    elif description_each in dic and sign == '-':
        dic[description_each] -= number
    elif description_each in dic and sign == '+':
        dic[description_each] += number


with pdfplumber.open("periods/15.03-30.05.pdf") as temp:
    page = 0
    plus = 0
    minus = 0
    period = re.findall(r'период.+', temp.pages[0].extract_text())
    try:
        while temp.pages[page].extract_text():
            first_page = temp.pages[page].extract_text()  # выбираем стр и вытаскиваем текст
            # print(first_page)
            what_date = re.findall(r'\d+.\d+.\d+\s\d+:', first_page)  # нашел даты на текущей стр
            for i in range(len(what_date)):
                current_date = ''.join(what_date[i][0:10]).split('.')  # пробегаемся по датам, найденным на стр
                if check_date(current_date):
                    # print(current_date)
                    sum = re.findall(r'[₽].{0,}[₽]', first_page)  # сумма
                    description = re.findall(r'[₽]\s\w.{0,}', first_page)  # описание
                    for i in range(len(description)):
                        description_each = description[i][2:]  # убираем ₽
                        sign = sum[i][2:3]  # знак
                        number = float(sum[i][4:].replace(',', '.').replace(' ', '').replace('₽', ''))  # цифра
                        if sign == '-':
                            minus -= number
                        else:
                            plus += number
                        description_each = abbreviation(description_each)
                        check_in_dic(description_each)
            page += 1
    except IndexError:
        pass

period = "".join(period)[9:].replace(' г. по ', '-').replace(' г.', '')

# print(dic)
# print(what_date)
# for i in dic:
#     print(i, dic[i])

# ---------------------Запись в файл--------------------------#
#
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
# ws = wb.create_sheet(period)
#
# num = 2
# _cell = ws['A1']
# _cell2 = ws['B1']
#
# _cell.value = 'Описание'
# _cell2.value = 'Сумма'
#
# for descr, sum in dic.items():
#     _cell = ws['A' + str(num)]  # Определяем необходимую ячейку на листе
#     _cell2 = ws['B' + str(num)]
#
#     _cell.value = descr  # Пишем в ячейке
#     _cell2.value = sum
#     num += 1
#     print(descr, '->', sum)
#
#
# # print(len(dic))
# totally = len(dic) + 3
#
# income = ws['A' + str(totally)]
# spent = ws['A' + str(totally+1)]
# total = ws['A' + str(totally+2)]
# income.value = "Пришло"
# spent.value = "Ушло"
# total.value = 'Всего'
#
# income_digit = ws['B' + str(totally)]
# spent_digit = ws['B' + str(totally+1)]
# total_digit = ws['B' + str(totally+2)]
# income_digit.value = plus
# spent_digit.value = minus
# total_digit.value = plus+minus
# save_workbook(wb, FILE_NAME)
