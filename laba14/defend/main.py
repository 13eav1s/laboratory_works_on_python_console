"""
Защита 14 лабораторной
ИУ7 11Б Краснов Леонид
Сортировка методом вставок
Ввести список целых чисел и отсортировать его
"""
import random


def InsSort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = cur
        print(i, ' : ', arr[:i], ' | ', arr[i:])
    return arr


col = int(input("Введите колличество элементов в списке: "))
mass = []
for i in range(col):
    mass.append(random.randint(0, 1000))
print("Не отсортированный список: ")
print(mass)
InsSort(mass)
print("Список после сортировки:")
print(mass)
