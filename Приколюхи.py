# проходка по индексам в словаре, без len
dic = {
    'one':1,
    'two':2,
}
for index, key in enumerate(dic): # enumerate - для получения индекса
    print(index, key)