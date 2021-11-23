"""
9. заполнить матрицу "змейкой" вида
...
9 8 7
4 5 6
3 2 1

Краснов Леонид ИУ7-11Б защита лабораторной №9
"""

N = int(input("Введите разимер матрицы: "))
matrix = []
for i in range(N):
    matrix.append([0] * N)

chislo = 1
for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        matrix[i][j] += chislo
        chislo += 1

for i in range(N):
    if i % 2 != 0:
        matrix[i].reverse()

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=" ")
    print()
