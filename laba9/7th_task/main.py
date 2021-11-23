"""
Лабораторная работа №9
Файл 7
ИУ7-11Б
Краснов Леонид
"""

# В этом списке хронятся гласные буквы
vowelLetters = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]

size = int(input("Введите размер матрицы: "))
matrix = []

# Цикл для заполнения матрицы элементами
for i in range(size):
    while True:
        D = list(map(str, input(f"Введите строку: ").split()))
        if len(D) == size:
            break
        else:
            print("Не верное колличество элементов")
    matrix.append(D)

# Вывод матрицы на экран
print("Матрица которую вы ввели:")
for i in range(size):
    for j in range(size):
        print("{:8s}".format(matrix[i][j]), end=" ")
    print()

for i in range(size):
    for j in range(size):
        if matrix[i][j] in vowelLetters:
            matrix[i][j] = "."

# Вывод матрицы на экран
print("Матрица без гласных букв:")
for i in range(size):
    for j in range(size):
        print("{:8s}".format(matrix[i][j]), end=" ")
    print()
