# """
# Задача 1: Запомнить первые положительные элементы каждой строки матрицы А в одномерный массив В. Если в строке нет
# положительных элементов, то в векторе не будет элемента.
# """
#
# A = []
# B = []
#
# size = int(input("Введите колличество элементов: "))
# for i in range(size):
#     D = list(map(float, input(f"Введите строку: ").split()))
#     A.append(D)
# for i in range(size):
#     for j in range(len(A[i])):
#         if A[i][j] > 0:
#             B.append(A[i][j])
#             break
#
# print("Перые положительные элементы: ")
# for i in range(len(B)):
#     print("{:5.2f}".format(B[i]), end=" ")


# """
# задача 2: Запомнить первые положительные элементы каждой строки матрицы A в одномерном массиве.
# Если в строке нет положительных элементов, то не добавлять в вектор ничего.
# """
#
# A = []
# B = []
#
# size = int(input("Введите колличество элементов: "))
# for i in range(size):
#     D = list(map(float, input(f"Введите строку: ").split()))
#     A.append(D)
# for i in range(size):
#     for j in range(len(A[i])):
#         if A[i][j] > 0:
#             B.append(A[i][j])
#             break
#
# print("Перые положительные элементы: ")
# for i in range(len(B)):
#     print("{:5.2f}".format(B[i]), end=" ")


"""
Задача 3: сформировать матрицу вида:
1 2 3 4 5
2 1 2 3 4
3 2 1 2 3
4 3 2 1 2
5 4 3 2 1
"""

size = int(input("Введите размер матрицы:"))
matrix = []
for i in range(size):
    matrix.append([0] * size)

# for i in range(size):
#     matrix[i][i] = 1

xxx = []
for i in range(size):
    xxx.append(i + 1)

x  = 0
for i in range(size):
    for j in range(size):

        matrix[i][j] = xxx[x]
        x += 1

for i in range(size):
    for j in range(size):
        print("{:8.2f}".format(matrix[i][j]), end=" ")
    print()
