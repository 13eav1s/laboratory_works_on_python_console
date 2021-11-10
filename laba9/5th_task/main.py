"""
Лабораторная работа №9
Файл 5
ИУ7-11Б
Краснов Леонид
"""

size = int(input("Введите размер матрицы: "))
matrixD = []

# Цикл для заполнения матрицы элементами
for i in range(size):
    while True:
        D = list(map(int, input(f"Введите строку: ").split()))
        if len(D) == size:
            break
        else:
            print("Не верное колличество элементов")
    matrixD.append(D)

# Вывод матрицы на экран
print("Матрица D:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(matrixD[i][j]), end=" ")
    print()


matrixZ = []
# Цикл для заполнения матрицы Z элементами
for i in range(size):
    while True:
        D = list(map(int, input(f"Введите строку: ").split()))
        if len(D) == size:
            break
        else:
            print("Не верное колличество элементов")
    matrixZ.append(D)

# Вывод матрицы на экран
print("Матрица Z:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(matrixZ[i][j]), end=" ")
    print()


massG = []

# Цикл для заполнения массива G
for i in range(size):
    sumElems = 0
    for j in range(size):
        sumElems += matrixZ[i][j]
    colElems = 0
    for j in range(size):
        if matrixD[i][j] > sumElems:
            colElems += 1
    massG.append(colElems)

# Умножение матрицы на наибольший элемен списка G
for i in range(size):
    for j in range(size):
        matrixD[i][j] *= max(massG)

# Вывод списка G на экран
print("G выглядит так: ")
for i in range(len(massG)):
    print("{:8d}".format(massG[i]), end=" ")
print()

# Вывод матрицы на экран
print("Матрица D:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(matrixD[i][j]), end=" ")
    print()
