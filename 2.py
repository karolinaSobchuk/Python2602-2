'''Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint

lenght = int(input('Введите длину списка: '))
st = list(randint(-10, 5) for i in range(lenght))
print(st)
min_st = int(input('Введите минимум значения: '))
max_st = int(input('Введите максимум значения: '))

for i in range (len(st)):
    if min_st <= st[i] <= max_st:
        print(f'Индексы элементов массива: {i}')

