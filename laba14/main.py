"""
Написать программу для демонстрации работы метода сортировки (по варианту) на
примере массива целых чисел.
Программа должна состоять из двух частей и выполнять два действия
последовательно: сначала отсортировать заданный пользователем массив, затем
составить таблицу замеров времени сортировки списков трёх различных (заданных
пользователем) размерностей. Для каждой размерности списка необходимо
исследовать:
● случайный список,
● отсортированный список,
● список, отсортированный в обратном порядке.
8. метод "расчески"
"""

import time


#  Функция для создания таблицы


def printTab(t1, t2, t3, t4, t5, t6, t7, t8, t9):
    tabsize = 69
    # построение таблицы
    print('_' * tabsize)
    print("|                                  |    N1    |     N2   |     N3   |")
    print('_' * tabsize)
    print("| Упорядоченный список             |{:10.5g}|{:10.5g}|{:10.5g}|".format(t1, t2, t3))
    print('_' * tabsize)
    print("| Случайный список                 |{:10.5g}|{:10.5g}|{:10.5g}|".format(t4, t5, t6))
    print('_' * tabsize)
    print("| Упорядоченный в обратном порядке |{:10.5g}|{:10.5g}|{:10.5g}|".format(t7, t8, t9))
    print('_' * tabsize)


#  Сортировка расческой из инета
# def sort(mass):
#     alen = len(mass)
#     gap = (alen * 10 // 13) if alen > 1 else 0
#     while gap:
#         if 8 < gap < 11:  # variant "comb-11"
#             gap = 11
#         swapped = False
#         for i in range(alen - gap):
#             if mass[i + gap] < mass[i]:
#                 mass[i], mass[i + gap] = mass[i + gap], mass[i]
#                 swapped = True
#         gap = (gap * 10 // 13) or swapped


#  Сортировка расчесткой
def hairbrush(mass):
    start_time = time.perf_counter()
    massLen = len(mass)
    redFac = 1.247
    gap = massLen - 1
    gapPose = gap
    colIter = 0
    gapF = 0
    while True:
        if gapPose >= massLen - 1:
            if colIter > 0:
                gap = int(massLen / (redFac * colIter))
            gapPose = gap
            gapF = 0
        colIter += 1
        while gapPose < massLen:
            if mass[gapF] > mass[gapPose]:
                x = mass[gapF]
                mass[gapF] = mass[gapPose]
                mass[gapPose] = x
                gapF += 1
                gapPose += 1
            else:
                gapF += 1
                gapPose += 1
        if gapPose - gapF == 1:
            print(mass)
            break
    t = time.perf_counter() - start_time
    return t


userMass1 = []
userMass2 = []
userMass3 = []
while True:
    try:
        option = (int(input("1 - Использовать готовый массив. \n2 - Ввести массив самостоятельно. "
                            "\nВыберите действие: ")))
        if 0 < option < 3:
            break
    except:
        print("Вы ввели не число!")
if option == 1:
    userMass1 = [300, 250, 200, 220, 300, 290, 280, 270, 200, 303, 200, 302, 123]
    userMass2 = [99, 32, 97, 12, 43, 54, 30, 12, 55]
    userMass3 = [3, 2, 2, 2, 3, 9, 8, 7, 2, 3, 2, 3, 1]
else:
    while True:
        try:
            sizeMass1 = int(input("Введите размер массива: "))
            if sizeMass1 > 0:
                break
            else:
                print("Размер должен быть больше нуля!")
        except:
            print("Вы ввели невозможный размер!")
    for i in range(sizeMass1):
        while True:
            try:
                userMass1.append(int(input("Введите элемент массива: ")))
                break
            except:
                print("Вы ввели не целое число")
    while True:
        try:
            sizeMass2 = int(input("Введите размер массива: "))
            if sizeMass2 > 0:
                break
            else:
                print("Размер должен быть больше нуля!")
        except:
            print("Вы ввели невозможный размер!")
    for i in range(sizeMass2):
        while True:
            try:
                userMass2.append(int(input("Введите элемент массива: ")))
                break
            except:
                print("Вы ввели не целое число")
    while True:
        try:
            sizeMass3 = int(input("Введите размер массива: "))
            if sizeMass3 > 0:
                break
            else:
                print("Размер должен быть больше нуля!")
        except:
            print("Вы ввели невозможный размер!")
    for i in range(sizeMass3):
        while True:
            try:
                userMass3.append(int(input("Введите элемент массива: ")))
                break
            except:
                print("Вы ввели не целое число")

time4 = hairbrush(userMass1)
time5 = hairbrush(userMass2)
time6 = hairbrush(userMass3)
time1 = hairbrush(userMass1)
time2 = hairbrush(userMass2)
time3 = hairbrush(userMass3)
userMass1.reverse()
userMass2.reverse()
userMass3.reverse()
time7 = hairbrush(userMass1)
time8 = hairbrush(userMass2)
time9 = hairbrush(userMass3)

printTab(time1, time2, time3, time4, time5, time6, time7, time8, time9)
#  print(hairbrush(userMass1))
#  print(timeit.timeit(hairbrush(userMass)))
#  printTab(1.314, 1234.432, 14.234, 1234, 123, 3, 354, 2.4, 23.34)
