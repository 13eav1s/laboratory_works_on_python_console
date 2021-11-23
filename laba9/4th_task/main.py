"""
Лабораторная работа №9
Файл 4 поворот матрицы
ИУ7-11Б
Краснов Леонид
"""

size = int(input("Введите размер матрицы: "))
matrix = []

# Цикл для заполнения матрицы элементами
for i in range(size):
    while True:
        D = list(map(int, input(f"Введите строку: ").split()))
        if len(D) == size:
            break
        else:
            print("Не верное колличество элементов")
    matrix.append(D)

# Вывод матрицы на экран
print("Матрица которую вы ввели:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(matrix[i][j]), end=" ")
    print()

# 00 01 02
# 10 11 12
# 20 21 22

# 20 10 00
# 21 11 01
# 22 12 02

# Поворот матрицы на 90 градусов по часовой стрелке
# Матрица, куда будет записан 1-я повернутая на 90
matrixFlip = []

# заполнение новой матрицы нулями
for i in range(size):
    matrixFlip.append([0] * size)

for i in range(size):
    for j in range(size):
        matrixFlip[i][j] = matrix[size - j - 1][i]

# Вывод матрицы на экран
print("Перевернутая по часовой матрица:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(matrixFlip[i][j]), end=" ")
    print()

# Поворот начальной матрицы против часовой на 90 градусов против часовой
matrixBackFlip = []

# заполнение новой матрицы нулями
for i in range(size):
    matrixBackFlip.append([0] * size)

# 00 01 02
# 10 11 12
# 20 21 22

# 02 12 22
# 01 11 21
# 00 10 20

# Запись перевернутой матрицы
for i in range(size):
    for j in range(size):
        matrixBackFlip[i][j] = matrix[j][size - i - 1]

# Вывод матрицы на экран
print("Перевернутая против часовой матрица:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(matrixBackFlip[i][j]), end=" ")
    print()
