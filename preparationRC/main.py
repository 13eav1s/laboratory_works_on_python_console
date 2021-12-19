"""
1. Даны 2 текстовых файла in1.txt и in2.txt, в которых записаны неубывающие последовательности
целых чисел, по одному числу в строке. Не используя списки и методы сортировки, сформировать
файл out.txt, в который записать неубывающую последовательность чисел, содержащую все числа
из исходных файлов. С файлами in1.txt и in2.txt работать построчно (в памяти единовременно
должно находится не более одной строки из каждого файла)
"""

# def rec(num1, num2):
#     if num1 == '' and num2 == '':
#         return 'Файлы кончились'
#     elif num1 == '':
#         out.write(num2 + '\n')
#         num2 = in2.readline().strip()
#         rec(num1, num2)
#     elif num2 == '':
#         out.write(num1 + '\n')
#         num1 = in1.readline().strip()
#         rec(num1, num2)
#     elif int(num1) < int(num2):
#         out.write(num1 + '\n')
#         num1 = in1.readline().strip()
#         rec(num1, num2)
#     elif num1 == num2:
#         out.write(num1 + '\n')
#         out.write(num2 + '\n')
#         num1 = in1.readline().strip()
#         num2 = in2.readline().strip()
#         rec(num1, num2)
#     else:
#         out.write(num2 + '\n')
#         num2 = in2.readline().strip()
#         rec(num1, num2)
#
#
# with open('in1.txt') as in1, open('in2.txt') as in2, open('out.txt', 'w') as out:
#     num1 = in1.readline().strip()
#     num2 = in2.readline().strip()
#     rec(num1, num2)


"""
2. В бинарном файле numbers.bin записана последовательность целых 8-байтных чисел (тип long-
long, фориат q в модуле struct). Требуется отсортировать его по возрастанию методом вставок и
затем вывести файл на экран. Считывать единовременно более двух чисел из файла в память
запрещено (в процессе сортировки требуется переставлять записи в самом файле).
"""

# def insertionSort(arr): #Сортировка вставками
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


def sort_file(filename, string_size):
    with open(filename, 'r+b') as f:
        lines = getsize(filename) // string_size
        for i in range(1, lines):
            f.seek(string_size * i)  # пропускаем число
            cur = struct.unpack('q', f.read(string_size))[0]
            j = i - 1
            f.seek(string_size * j)
            n = struct.unpack('q', f.read(string_size))[0]
            while j >= 0 and cur < n:
                f.write(struct.pack('q', n))
                j -= 1
                f.seek(string_size * (j + 1))
                f.write(struct.pack('q', cur))
                if j >= 0:
                    f.seek(string_size * j)
                    n = struct.unpack('q', f.read(string_size))[0]
