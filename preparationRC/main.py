"""
1. Даны 2 текстовых файла in1.txt и in2.txt, в которых записаны неубывающие последовательности
целых чисел, по одному числу в строке. Не используя списки и методы сортировки, сформировать
файл out.txt, в который записать неубывающую последовательность чисел, содержащую все числа
из исходных файлов. С файлами in1.txt и in2.txt работать построчно (в памяти единовременно
должно находится не более одной строки из каждого файла)
"""

# #  Главная функция программы
# #  strip используется для удаления символов прерноса строки
# def rec(numb1, numb2):
#     if numb1 == '' and numb2 == '':  # Проверка на то что оба файла кончились
#         return 'Файлы кончились'  # Выход из функции
#     elif numb1 == '':  # Проверка на то что кончился первый файл
#         out.write(numb2 + '\n')  # вывод значения из второго файла в третий
#         numb2 = in2.readline().strip()  # чтение следующего значения из второго файла
#         rec(numb1, numb2)  # Вызов этой функции заново
#     elif numb2 == '':  # Проверка на то что 2 файл кончился
#         out.write(numb1 + '\n')  # Вывод значения из первого файла в 3-й
#         numb1 = in1.readline().strip()  # Чтение следующего значения из первого файла
#         rec(numb1, numb2)  # Вызов этой функции заново
#     elif int(numb1) < int(numb2):  # Сравнивание значения из первого файла и второго
#         out.write(numb1 + '\n')  # Вывод меньшего в третий файл
#         numb1 = in1.readline().strip()  # Чтение следующего значения из первого файла
#         rec(numb1, numb2)  # Вызов этой функции заного
#     elif numb1 == numb2:  # Проверка на равенство значений из файлов
#         out.write(numb1 + '\n')  # Запись значения из первого файла в третий
#         out.write(numb2 + '\n')  # Запись значения из второго файла в перывй
#         numb1 = in1.readline().strip()  # Чтение следующего значения из первого файла
#         numb2 = in2.readline().strip()  # Чтение следующего значения из второго файла
#         rec(numb1, numb2)  # Вызов этой функции заного
#     else:  # Срабатывает если значение из первого файла, больше заначения из первого
#         out.write(numb2 + '\n')  # Вывод значения из второго файла в третий
#         numb2 = in2.readline().strip()  # Чтение следующего значения из второго файла
#         rec(numb1, numb2)  # Вызов этой функции заново
#
#
# #  Точка входа в программу
# with open('in1.txt') as in1, open('in2.txt') as in2, open('out.txt', 'w') as out:
#     num1 = in1.readline().strip()  # Переменная для записи значения из файла in1.txt
#     num2 = in2.readline().strip()  # Переменная для записи заначения из файла in2.txt
#     rec(num1, num2)  # Рекурсионная функция


"""
2. В бинарном файле numbers.bin записана последовательность целых 8-байтных чисел (тип long-
long, фориат q в модуле struct). Требуется отсортировать его по возрастанию методом вставок и
затем вывести файл на экран. Считывать единовременно более двух чисел из файла в память
запрещено (в процессе сортировки требуется переставлять записи в самом файле).
"""


#  Сортировка вставками
# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         cur = arr[i]
#         j = i - 1
#         while (j >= 0 and cur < arr[j]):
#             arr[j + 1] = arr[j]
#             j = j - 1
#             arr[j + 1] = cur
#         print(i,' : ', arr[:i], ' | ', arr[i:])
#     return arr


import struct
from os.path import getsize


def sort_file(filename, stringLen):
    with open(filename, 'r+b') as f:
        lines = getsize(filename) // stringLen
        for i in range(1, lines):
            f.seek(stringLen * i)  # пропускаем число
            cur = struct.unpack('q', f.read(stringLen))[0]
            j = i-1
            f.seek(stringLen * j)
            n = struct.unpack('q', f.read(stringLen))[0]
            while j >= 0 and cur < n:
                f.write(struct.pack('q', n))
                j -= 1
                f.seek(stringLen * (j + 1))
                f.write(struct.pack('q', cur))
                if j >= 0:
                    f.seek(stringLen * j)
                    n = struct.unpack('q', f.read(stringLen))[0]


# для проверки (лажовый код не смотрите)
string_size = struct.calcsize('q')
with open('numbers.bin', 'wb') as f1:
    f1.write(struct.pack('q', 556))
    f1.write(struct.pack('q', 32))
    f1.write(struct.pack('q', 0))
    f1.write(struct.pack('q', 123))
    f1.write(struct.pack('q', 23))
sort_file('numbers.bin', string_size)
with open('numbers.bin', 'rb') as f1:
    print(struct.unpack('q', f1.read(string_size))[0])
    print(struct.unpack('q', f1.read(string_size))[0])
    print(struct.unpack('q', f1.read(string_size))[0])
    print(struct.unpack('q', f1.read(string_size))[0])
    print(struct.unpack('q', f1.read(string_size))[0])
