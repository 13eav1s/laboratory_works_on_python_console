"""
Лабораторная работа №9
Файл 9 Трехмерный массив
ИУ7-11Б
Краснов Леонид
"""

# Создание трехмерного массива
mass3 = []
X = int(input("Введите размеры массива по X: "))
Y = int(input("Введите размеры массива по Y: "))
Z = int(input("Введите размеры массива по Z: "))
for x in range(X):
    mass2 = []
    for y in range(Y):
        while True:
            String = list(map(int, input(f"Введите строку: ").split()))
            if len(String) == Z:
                break
            else:
                print("Вы ввели неверное колличество элементов!")
        mass2.append(String)
    mass3.append(mass2)

# Вывод трехмерного массива
print("Трехмерный массив: ")
for x in range(X):
    for y in range(Y):
        for z in range(Z):
            print((mass3[x][y][z]), end=" ")
        print()
    print()

print("Другой вид: ")
print(mass3)

while True:
    i = int(input("ввдите номер среза по второму индексу: "))
    if i >= Y:
        print("Вы ввели слишком большой индекс")
    else:
        break

for x in range(X):
    print(mass3[x][i])
