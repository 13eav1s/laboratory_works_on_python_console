"""
Написать программу, которая позволит с использованием меню обеспечить работу с
целочисленными матрицами:
1. Ввести матрицу
2. Добавить строку
3. Удалить строку
4. Добавить столбец
5. Удалить столбец
6. Найти строку, имеющую определённое свойство по варианту
7. Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов
8. Найти столбец, имеющий определённое свойство по варианту
9. Переставить местами столбцы с максимальной и минимальной суммой
элементов
10. Вывести текущую матрицу
"""


def PrintMenu():
    print("Меню: \n"
          "1. Ввести матрицу \n"
          "2. Добавить строку \n"
          "3. Удалить строку \n"
          "4. Добавить столбец \n"
          "5. Удалить столбец \n"
          "6. Найти строку, имеющую определённое свойство по варианту \n"
          "7. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов \n"
          "8. Найти столбец, имеющий определённое свойство по варианту \n"
          "9. Переставить местами столбцы с максимальной и минимальной суммойэлеметов \n"
          "10. Вывести текущую матрицу \n"
          "0. Выйти из программы \n")
    while True:
        elem = int(input("Введите номер пункта: "))
        if 0 <= elem <= 7:
            break
    return elem


def ClearArray(matrix):
    matrix.clear()
    print("Матрица очищена")
    return matrix


def OutMatrix(a):
    print("Матрица выглядит так: ")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()
    print()
    return 0


def ClearAndFill(matrix):
    ClearArray(matrix)
    matrix_column = int(input("Введите колличество столбцов: "))
    matrix_string = int(input("Введите колличество строчек: "))
    for i in range(matrix_string):
        matrix.append([0]*matrix_column)
    for i in range(matrix_string):
        for j in range(matrix_column):
            matrix[i][j] = int(input("Введите элемент, который хотите добавить: "))
    OutMatrix(matrix)
    return matrix


def AddString(matrix):
    matrix.append([0]*len(matrix[0]))
    for i in range(len(matrix[0])):
        matrix[len(matrix) - 1][i] = int(input("Введите элемент который хотите добавить: "))
    OutMatrix(matrix)


def DelString(matrix):
    index = int(input("Введите номер строки, которую хотите удалить: "))
    matrix.pop(index)
    OutMatrix(matrix)


mass = []
item = PrintMenu()
while True:
    if item == 0:
        print("Программа завершила работу")
        break
    if item == 1:
        ClearAndFill(mass)
        item = PrintMenu()
    if item == 2:
        AddString(mass)
        item = PrintMenu()
    if item == 3:
        DelString(mass)
        item = PrintMenu()
    if item == 10:
        OutMatrix(mass)
        item = PrintMenu()
