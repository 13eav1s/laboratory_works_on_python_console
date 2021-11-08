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
          "6. Найти строку наибольшее количество подряд идущих одинаковых элементов \n"
          "7. Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов \n"
          "8. Найти столбец, имеющий наибольшее колличество четных элементов \n"
          "9. Переставить местами столбцы с максимальной и минимальной суммой элеметов \n"
          "10. Вывести текущую матрицу \n"
          "0. Выйти из программы \n")
    while True:
        elem = int(input("Введите номер пункта: "))
        if 0 <= elem <= 10:
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


def ClearAndFill(matrix):
    ClearArray(matrix)
    matrix_column = int(input("Введите колличество столбцов: "))
    matrix_string = int(input("Введите колличество строчек: "))
    for i in range(matrix_string):
        matrix.append([0] * matrix_column)
    for i in range(matrix_string):
        for j in range(matrix_column):
            matrix[i][j] = int(input("Введите элемент, который хотите добавить: "))
    OutMatrix(matrix)
    return matrix


def AddString(matrix):
    index = int(input("Введите номер строки, которую хотите добавить: "))
    if index > len(matrix):
        print("Матрица меньше, чем вы думаете")
        return 0
    if index == len(matrix):
        matrix.append([0] * len(matrix[0]))
        for i in range(len(matrix[0])):
            matrix[len(matrix) - 1][i] = int(input("Введите элемент, который хотите добавить: "))
        OutMatrix(matrix)
        return matrix
    newString = []
    for i in range(len(matrix[0])):
        newString.append(int(input("Введите элемент, который хотите добавить: ")))
    matrix.insert(index, newString)
    OutMatrix(matrix)
    return matrix


def DelString(matrix):
    index = int(input("Введите номер строки, которую хотите удалить: "))
    if index >= len(matrix):
        print("Нет такой строки ")
        return 0
    matrix.pop(index)
    OutMatrix(matrix)
    return matrix


def DelColumn(matrix):
    index = int(input("Введите номер колонки, которую хотите удалить: "))
    for i in range(len(matrix)):
        matrix[i].pop(index)
    OutMatrix(matrix)
    return matrix


def AddColumn(matrix):
    print("Вы выбрали добавить столбец ")
    index = int(input("Введите номер столбца который хотите добавить: "))
    if index > len(matrix[0]):
        print("Матрица меньше чем вы думаете")
        return 0
    if index == len(matrix[0]):
        for i in range(len(matrix)):
            matrix[i].append(int(input("Введите элемент, который хотите добавить: ")))
        OutMatrix(matrix)
        return matrix
    for i in range(len(matrix)):
        matrix[i].insert(index, int(input("Введите элемент, который хотите добавить: ")))
    OutMatrix(matrix)
    return matrix


def FindCommonString(matrix):
    num = 0
    numlast = 0
    maxindex = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == matrix[i][j + 1]:
                num += 1
                if num > numlast:
                    numlast = num
                    maxindex = i
            else:
                num = 0
    print("Строчка с максимальным колличеством подряд идущих символов: \n", matrix[maxindex])


def ReplaceStrings(matrix):
    lastmax = 0
    lastmin = 0
    minindex = 0
    maxindex = 0
    for i in range(len(matrix)):
        elem = 0
        for j in range(len(matrix[i])):
            if int(matrix[i][j]) < 0:
                elem += 1
                if lastmax < elem:
                    lastmax = elem
                    maxindex = i
                if lastmin > elem:
                    lastmin = elem
                    minindex = i
    save_string = matrix[maxindex]
    matrix[maxindex] = matrix[minindex]
    matrix[minindex] = save_string
    OutMatrix(matrix)


def ReplaceColums(matrix):
    maxsum = -100500
    minsum = 100500
    minindex = 0
    maxindex = 0
    for i in range(len(matrix[0])):
        tempSum = 0
        for j in range(len(matrix)):
            tempSum += matrix[j][i]
        if tempSum > maxsum:
            maxsum = tempSum
            maxindex = i
        if tempSum < minsum:
            minsum = tempSum
            minindex = i
    # print("maxindex =",  maxindex, "minindex =", minindex)
    save_column = []
    for i in range(len(matrix)):
        save_column.append(matrix[i][maxindex])
    for i in range(len(matrix)):
        matrix[i][maxindex] = matrix[i][minindex]
    for i in range(len(matrix)):
        matrix[i][minindex] = save_column[i]
    OutMatrix(matrix)


def findColumn(matrix):
    maxcol = 0
    index = 0
    for i in range(len(matrix[0])):
        col = 0
        for j in range(len(matrix)):
            if matrix[j][i] % 2 == 0:
                col += 1
                if col > maxcol:
                    maxcol = col
                    index = i
    print("Столбец с наибольшим колличеством четных элементов имеет индекс: ", index)
    for i in range(len(matrix)):
        print(matrix[i][index])
    return matrix


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
    if item == 4:
        AddColumn(mass)
        item = PrintMenu()
    if item == 5:
        DelColumn(mass)
        item = PrintMenu()
    if item == 6:
        FindCommonString(mass)
        item = PrintMenu()
    if item == 7:
        ReplaceStrings(mass)
        item = PrintMenu()
    if item == 8:
        findColumn(mass)
        item = PrintMenu()
    if item == 9:
        ReplaceColums(mass)
        item = PrintMenu()
    if item == 10:
        OutMatrix(mass)
        item = PrintMenu()
