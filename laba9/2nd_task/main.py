"""
Лабораторная работа №9
2-й файл
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

# В этот массив будут записываться элементы над главной диагональю
upElems = []
# В этот массив будут записываться элементы под главной диагональю
lowElems = []

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

# Цикл для нахождения элементов над и под главной диагональю и
# записи их в соответствующие массивы
for i in range(size):
    for j in range(size):
        if i < j:
            upElems.append(matrix[i][j])
        elif i > j:
            lowElems.append(matrix[i][j])

# Проверка правильности работы программы
# print("upElems =", upElems)
# print("lowElems = ", lowElems)

print("Максимальный элемент над главной диагональю =", max(upElems))
print("Минимальный элемент под главной диагональю =", min(lowElems))
