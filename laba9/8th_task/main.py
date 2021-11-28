"""
Лабораторная работа №9
Файл 8
ИУ7-11Б
Краснов Леонид
"""

size = int(input("Введите размер матрицы: "))

# Две начальные матрицы
A = []
B = []

# Цикл для заполнения матрицы элементами
print("Заполните матрицу A")
for i in range(size):
    while True:
        D = list(map(int, input(f"Введите строку: ").split()))
        if len(D) == size:
            break
        else:
            print("Не верное колличество элементов")
    A.append(D)


# Цикл для заполнения матрицы элементами
print("Заполните матрицу B")
for i in range(size):
    while True:
        D = list(map(int, input(f"Введите строку: ").split()))
        if len(D) == size:
            break
        else:
            print("Не верное колличество элементов")
    B.append(D)

# Объявление и заполнение матрицы C нулями
C = []
for i in range(size):
    C.append([0] * size)

# Заполнение матрицы произведением элементов из A и B
for i in range(size):
    for j in range(size):
        C[i][j] = A[i][j] * B[i][j]

# Объявление массива в который будет записана сумма элементов из каждого столбца матрицы C
V = []

for i in range(size):
    sumElems = 0
    for j in range(size):
        sumElems += C[j][i]
    V.append(sumElems)

# Вывод матрицы на экран
print("Матрица A: ")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(A[i][j]), end=" ")
    print()

# Вывод матрицы на экран
print("Матрица B:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(B[i][j]), end=" ")
    print()

# Вывод матрицы на экран
print("Матрица C:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(C[i][j]), end=" ")
    print()

# Вывод массива V
print("Массив V:")
for i in range(size):
    print("{:8d}".format(V[i]), end=" ")
print()
