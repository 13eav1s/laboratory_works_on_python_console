"""
Защита лабораторной работы №4
ИУ7 - 11Б
Краснов Леонид
"""

import math as m

begin_value = float(input('Введите начальное значение диапазона '
                          'аргумента: '))
end_value = float(input('Введите конечное значение'
                        ' диапазона аргумента: '))
step = float(input('Введите шаг аргумента: '))
step_value = (end_value - begin_value) / step

# Задание начальных значений для максимальных и минимальных значений
# функций
# Хранится минимальное значение функции s
s_min = begin_value**2 + 1
# Хранится максимальное значение функции s
s_max = begin_value**2 + 1

i = 0
while i <= (abs((end_value - begin_value) / step)):
    x = begin_value + step * i
    s = x**2 + 1  # Функция
    if s > s_max:  # Нахождение максимального значения s
        s_max = s
    elif s < s_min:
        s_min = s  # Нахождение минимального значения s
    i += 1
# Колличество засечек
sum_serifs = 2
print()
# Нахождение масштаба для графика
scale = (s_max - s_min) / (sum_serifs - 1)
# Счетчик значений
i = 0
# вывод оси Y
# Колличество пробелов между численными обозначениями засечек
gaps = 13
print(' ' * (gaps - 5), end='', sep='')
while i < sum_serifs:
    serifs = s_min + scale * i
    if serifs > 0:
        indent = 12
    else:
        indent = 13
    if i != 0:
        print(' ' * (m.ceil(100 / (sum_serifs - 1)) - indent),
              '{:e}'.format(serifs), end='', sep='')
    else:
        print('{:e}'.format(serifs), end='', sep='')
    i += 1
print()
i = 0
while i < sum_serifs + 1:
    if i == sum_serifs:
        print('->y', sep='', end='')
    elif i != 0:
        print('-' * (m.ceil(100 / (sum_serifs - 1)) - 1), '|', sep='',
              end='')
    else:
        print(' ' * gaps, '-', '|', sep='', end='')
    i += 1
amount_column = m.ceil(100 / (sum_serifs - 1)) * (sum_serifs - 1)
delta = (s_max - s_min) / amount_column
if s_min > 0:
    zero_column = 0
elif s_max < 0:
    zero_column = m.ceil(100 / (sum_serifs - 1)) \
                  * (sum_serifs - 1) + 2
else:
    zero_column = m.ceil(-s_min / delta) + 1
print()
i = 0
# Вывод графика
while i <= (m.floor((end_value - begin_value) / step)):
    x = begin_value + step * i
    s = x**2 + 1  # Та-же функция
    if s != s_min:
        amount_space = int(
            ((s - s_min) / (s_max - s_min)) * amount_column) + 1
    else:
        amount_space = 1
    if s >= 0:
        n = zero_column + 1
        amount_space += 1
    else:
        n = zero_column
    print('{:e}'.format(s), end='', sep='')  # Вывод оси X
    if n == amount_space:
        print(amount_space * ' ', '*', sep='')
    if n < amount_space:
        print(n * ' ', '|', sep='', end='')
        print((amount_space - n - 1) * ' ', '*', sep='')
    else:
        print(amount_space * ' ', '*', sep='', end='')
        print((n - amount_space - 1) * ' ', '|', sep='')
    i += 1
