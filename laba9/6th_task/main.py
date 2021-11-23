"""
Лабораторная работа №9
Файл 6
ИУ7-11Б
Краснов Леонид
"""

size = int(input("Введите размер матрицы: "))
D = []

# Цикл для заполнения матрицы элементами
for i in range(size):
    while True:
        A = list(map(int, input(f"Введите строку: ").split()))
        if len(A) == size:
            break
        else:
            print("Не верное колличество элементов")
    D.append(A)

# Массив в котором хранятся номера строк
while True:
    I = list(map(int, input(f"Введите номера строк: ").split()))
    flag = 0
    for i in range(len(I)):
        if I[i] < size:
            pass
        else:
            print("Вы хотя бы один из индексов слишком большой")
            flag = 1
        if flag == 1:
            break
    if flag == 0:
        break


# В этот массив будут записаны максимальные элементы
R = []

# Цикл для нахождения и записи максимальных элементов в строке
for i in range(len(I)):
    maxElem = 0
    R.append(max(D[I[i]]))

# Вывод матрицы на экран
print("Матрица D:")
for i in range(size):
    for j in range(size):
        print("{:8d}".format(D[i][j]), end=" ")
    print()

print("Массив I:")
print(I)

print("Массив R:")
print(R)
average = sum(R) / len(R)
print("Среднеарифметическое = ", average)
