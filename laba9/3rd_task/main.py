"""
Лабораторная работа №9
Файл 3
Транспонирование матрицы
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

# 00 10 20
# 01 11 21
# 02 12 22

# Вывод матрицы на экран в транспонированном виде
print("Транспонированная матрица:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(matrix[j][i]), end=" ")
    print()
