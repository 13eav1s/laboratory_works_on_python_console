"""
Написать программу, которая в консоле рисует график функции звездочками, а также выводит таблицу значений функции.
Автор Краснов Леонид
"""
import math as m

begin_value = float(input('Введите начальное значение диапазона '
                          'аргумента: '))
end_value = float(input('Введите конечное значение'
                        ' диапазона аргумента: '))
step = float(input('Введите шаг аргумента: '))
step_value = (end_value - begin_value) / step
# построение таблицы
print('_' * 65)
print('|     номер     |   значение x  |  значение s1  |  значение s2  |')
print('_' * 65)

# Задание начальных значений для максимальных и минимальных значений
# функций
# Хранится минимальное значение функции s1
s_min2 = m.tan(0.2 * begin_value + 0.3) - begin_value ** 2 + 3
# Хранится максимальное значение функции s1
s_max2 = m.tan(0.2 * begin_value + 0.3) - begin_value ** 2 + 3
# Хранится максимальное значение функции s2
s_max1 = m.sqrt(begin_value) - 2 * m.cos((m.pi / 2) * begin_value)
# Хранится минимальное значение функции s2
s_min1 = m.sqrt(begin_value) - 2 * m.cos((m.pi / 2) * begin_value)

i = 0
while i <= (abs((end_value - begin_value) / step)):
    x = begin_value + step * i
    if x >= 0:
        s1 = m.sqrt(x) - 2 * m.cos((m.pi / 2) * x)  # Функция 1
    else:
        s1 = -0
    s2 = m.tan(0.2 * x + 0.3) - x ** 2 + 3  # Функция 2
    print('|{:15.0g}|{:15.5g}|{:15.5g}|{:15.5g}|'
          .format(i, x, s1, s2))
    if s2 > s_max2:  # Нахождение максимального значения s2
        s_max2 = s2
    elif s2 < s_min2:
        s_min2 = s2  # Нахождение минимального значения s2
    if s1 > s_max1:  # Нахождение максимального значения s1
        s_max1 = s1
    elif s1 < s_min1:
        s_min1 = s1  # Нахождение минимального значения s1
    i += 1
    print('_' * 65)
# Ввод количества засечек
sum_serifs = int(input("Введите кол-во делений от 4 до 8: "))
print()
# Нахождение масштаба для графика
scale = (s_max2 - s_min2) / (sum_serifs - 1)
# Счетчик значений
i = 0
# вывод оси Y
# Колличество пробелов между численными обозначениями засечек
gaps = 13
print(' ' * (gaps - 5), end='', sep='')
while i < sum_serifs:
    serifs = s_min2 + scale * i
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
delta = (s_max2 - s_min2) / amount_column
if s_min2 > 0:
    zero_column = 0
elif s_max2 < 0:
    zero_column = m.ceil(100 / (sum_serifs - 1)) \
                  * (sum_serifs - 1) + 2
else:
    zero_column = m.ceil(-s_min2 / delta) + 1
print()
i = 0
# Вывод графика
while i <= (m.floor((end_value - begin_value) / step)):
    x = begin_value + step * i
    if x >= 0:
        s1 = m.sqrt(x) - 2 * m.cos((m.pi / 2) * x)  # Та-же функция 1
    s2 = m.tan(0.2 * x + 0.3) - x ** 2 + 3  # Та-же вторая функция 2
    if s2 != s_min2:
        amount_space = int(
            ((s2 - s_min2) / (s_max2 - s_min2)) * amount_column) + 1
    else:
        amount_space = 1
    if s2 >= 0:
        n = zero_column + 1
        amount_space += 1
    else:
        n = zero_column
    print('{:e}'.format(s2), end='', sep='')
    if n == amount_space:
        print(amount_space * ' ', '*', sep='')
    elif n < amount_space:
        print(n * ' ', '|', sep='', end='')
        print((amount_space - n - 1) * ' ', '*', sep='')
    else:
        print(amount_space * ' ', '*', sep='', end='')
        print((n - amount_space - 1) * ' ', '|', sep='')
    i += 1
