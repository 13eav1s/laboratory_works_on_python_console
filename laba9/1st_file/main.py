"""
Лабораторная работа №9 1-й файл
ИУ7-11Б
Краснов Леонид
"""

import math as m


D = list(map(float, input(f"Введите строку: ").split()))
F = list(map(float, input(f"Введите строку: ").split()))
a = []
for i in range(len(D)):
    a.append([0]*len(F))

for j in range(len(D)):
    for k in range(len(F)):
        a[j][k] = m.sin(D[j] + F[k])
# print("Матрица выглядит так: ")
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=" ")
#     print()
average = 0
AV = []
L = []

for i in range(len(a)):
    plusElem = 0
    for j in range(len(a[i])):
        if a[i][j] >= 0:
            average += a[i][j]
            plusElem += 1
    if plusElem == 0:
        average = 0
    else:
        average /= plusElem
    # print("Среднеарифметическое", i, "строки = ", average)
    AV.append(average)
    lowElem = 0
    for j in range(len(a[i])):
        if a[i][j] < average:
            lowElem += 1
    L.append(lowElem)
    average = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print("     ", AV[i], L[i], end=" ")
    print()