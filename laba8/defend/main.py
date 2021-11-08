"""
Защита лабы номер 8
Краснов Леонид ИУ7-11Б
Удаление главной диагонали квадратной матрицы таким образом, чтобы в матрице стало на 1 строку меньше.
00 01 02
10 11 12
20 21 22

10 01 02
20 21 12
"""

a = int(input("Введите длину квадратной матрицы: "))
matrix = []
for i in range(a):
    matrix.append([0] * a)

for i in range(a):
    for j in range(a):
        matrix[i][j] = int(input("Введите элемент матрицы: "))

print("Матрица выглядит так")
for i in range(a):
    for j in range(a):
        print(matrix[i][j], end=" ")
    print()
print("_____________________")

for i in range(a - 1):
    for j in range(a):
        if i == j:
            matrix[i][j] = matrix[i+1][j]
        elif i > 0 and i + 1 != j:
            matrix[i][j] = matrix[i+1][j]

matrix.pop(a - 1)

print("Матрица выглядит так: ")
for i in range(a - 1):
    for j in range(a):
        print(matrix[i][j], end=" ")
    print()
