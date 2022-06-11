def abbreviation(description_each):

    if "8199515993" in description_each:
        # print(description_each)
        return 'Сберегательный счет'
    elif 'Delivery'in description_each:
        return 'Delivery club'
    elif 'Apteka' in description_each or 'MSKAPT' in description_each:
        return 'Аптека'
    elif '79851721900' in description_each or '5106983603' in description_each:
        return 'Антоха'
    elif 'SBERMARKET' in description_each:
        return 'Сбермаркет'
    elif '79831123953' in description_each:
        return 'Настя'
    elif 'MIMOZA' in description_each:
        return 'Столовая'
    elif '79244230810' in description_each:
        return 'Себе на Альфа Банк'
    elif 'OKEY' in description_each:
        return 'OKEY'
    elif 'VODNY STADION' in description_each or 'Moscow Central Circle' in description_each or 'SHABOLOVSKAYA' in description_each:
        return 'Метро'
    elif '5465455276' in description_each:
        return 'Наташа'
    elif 'YM*DRIVE' in description_each:
        return 'Яндекс Драйв'
    elif 'GIBDD' in description_each:
        return 'Штрафы ГИБДД'
    elif 'MTS' in description_each:
        return 'MTS'
    elif 'MOSKVICHKA' in description_each:
        return 'Парикмахерская'
    elif 'wildberries' in description_each.casefold():
        return 'Wildberries'
    elif 'PYATEROCHKA' in description_each:
        return 'Пятерочка'
    elif 'Whoosh' in description_each or 'Urent' in description_each:
        return 'Самокат'
    elif 'VKUSVILL' in description_each:
        return 'VKUSVILL'
    elif 'POST' in description_each:
        return 'Почта'
    elif 'MegaFon'.casefold() in description_each.casefold():
        return 'Мегафон'
    elif 'yandex.plus' in description_each.lower():
        return 'Яндекс Плюс'
    elif 'CVETOV' in description_each:
        return 'Цветы'
    elif 'KRASNOE' in description_each:
        return 'Красно Белое'
    elif 'MAGNOLIYA' in description_each:
        return 'Магнолия'
    elif 'Centralnaya PPK' in description_each:
        return 'Поездка загород'
    elif 'Yandex.Market' in description_each:
        return 'Яндекс Маркет'
    elif 'DIXY' in description_each:
        return 'Дикси'
    elif 'PEREKRESTOK' in description_each:
        return 'Перекресток'



    return description_each

    # elif 'Внешний банковский перевод на счёт' in description_each:
    #     return 'Квартира'