import pdfplumber
import re
dic = {}
page = 0
plus = 0
minus = 0
'''
main ветка
'''
with pdfplumber.open("list_new.pdf") as temp:
  try:
    # while temp.pages[page].extract_text():
    first_page = temp.pages[page].extract_text() # выбираем стр и вытаскиваем текст
    page += 1
    print(first_page)
    # date = re.findall(r'\d\d[.]\d\d[.]\d{4}\s\d\d[:]\d\d', first_page)
    sum = re.findall(r'[₽].{0,}[₽]', first_page)  # сумма
    # print(sum[0])
    description = re.findall(r'[₽]\s\w.{0,}', first_page)  # описание
    # print(description)
    # for i in range(len(description)):
    #   description_each =description[i][2:]  # убираем ₽
    #   sign = sum[i][2:3]  # знак
    #   number = float(sum[i][4:].replace(',', '.').replace(' ', ''))  # цифра
    #
    #   if description_each not in dic:
    #     if sign == "+":
    #       dic[description_each] = number
    #       plus += number
    #     else:
    #       dic[description_each] = float('-'+ str(number))
    #       minus += number
    #   else:
    #     if sign == "+":
    #       dic[description_each] += number
    #       plus += number
    #     else:
    #       dic[description_each] -= number
    #       minus += number
  except IndexError:
    pass
print(sum)
print(plus, minus)


#
# for i in dic:
#   print(i, dic[i])






  # print(first_page)
  # first_page = first_page.split('\n')  # разделяем его по /n
  #
  # for i in first_page:
  #   if len(i.split(' ')[0]) == 10:  # доходим до столбца "дата"
  #     date = i.split(' ')[0]+', '+i.split(' ')[1]  # дата и время
  #     in_out_come = i.split(' ')[3]
  #     total = i.split()[4].split('₽') + i.split()[5].split('₽')  # первая и вторая часть суммы разъеденины
  #     amount = float(total[0].replace(',','.') + total[1].replace(',','.'))  # складываем первую и вторую часть
  #     # print(in_out_come, amount)
  #     # print(total,amount)
  #     # amount2 = i.split(' ')[5].split('₽')[0].replace(',','.').strip()
  #     # try:
  #     #   amount2 = str(float(amount2))
  #     # except ValueError:
  #     #   pass
  #     # print(amount, amount2)
  #     # print(i.split())

