"""
Задана символьная матрица. Создать вектор, в который записать среднее арифметическое числовых элементов каждого столбца,
в котором есть цифры. Далее необходимо заменить символом "#" все элементы строк и столбцов, в которых есть заглавные
латинские буквы. Дополнительных матриц не использовать. Разрешено использовать один одномерный массив, размером не более
максимального размера матрицы.
"""

matrix = []
while True:
    String = input("Введите элементы: ").split()
    if len(String) == 0:
        break
    matrix.append(String)

vector = []

for i in range(len(matrix[0])):
    sum = 0
    col = 0
    for j in range(len(matrix)):
        if matrix[j][i].isdigit():
            col += 1
            sum += int(matrix[j][i])
    if col != 0:
        vector.append(sum / col)

print("Vector: ")
for x in vector:
    print(x)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        for c in matrix[i][j]:
            if ord("Z") >= ord(c) >= ord("A"):
                matrix[i][j] = "#"
                break

print("Матрица с решотками: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
