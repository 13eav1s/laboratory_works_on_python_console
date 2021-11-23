"""
Программа для вычисления приближенного значения интеграла двумя разными методами
1. трапицией
2. Буля
Входные данные:
Начало отрезка
Конец отрезка
N1, N2 - Колличества участков разбиения для численного интегрирования.
Далее постороить таблицу

На основе известной первообразной определить, какой метод является наиболее
точным (указав обслютную погрешность измерения), а для менее точного метода
тиерационно вычислить количество участков разбиения, для которого
интерал будет вычислен с заданной точностью:
|I(N) - I(2N)| < E

Интегрируемую функцию и превообразную необходимо описать в виде программных
функций, что бы их можно было легко заменить на произвольные и убедиться, что
программа работает корректно.
"""


# функция для задания функции
def Y(x):
    y = x ** 2  # + 2 * x + 10
    return y


# Функция для метода трапеций
def Trapezoid(A, B, N):
    h = (B - A) / N
    x = A
    rez = 0
    while x < B - h:
        rez += ((Y(x) + Y(x + h)) / 2) * ((x + h) - x)
        x += h
    return rez


# Функция для метода Буля
def Bull(start, stop, N):
    if N % 4 != 0:
        print("Происходит округление....")
        while N % 4 != 0:
            N += 1
        print("N для метода Буля равно ", N)
    h = (stop - start) / N
    I = 2 * h / 45
    rez = 0
    x = start
    i = 0
    flag = 0
    cof = 7
    while x <= stop:
        if i % 2 == 0:
            rez += cof * Y(x)
            # print(cof)
            if cof == 7:
                cof = 12
            elif cof == 12 and flag == 0:
                cof = 14
            elif cof == 14:
                flag = 1
                cof = 12
            elif cof == 12 and flag == 1:
                cof = 7
                flag = 0
        else:
            rez += 32 * Y(x)
            # print(32)
        i += 1
        x += h
    rez *= I
    return rez


# Точка входа в программу
# Получение начальных данных с клавиатуры
start = float(input("Введите начало: "))
stop = float(input("Введите конец: "))
N1 = int(input("Введите N1: "))
N2 = int(input("Введите N2: "))


# Вывод значений
print("       |    N1    |     N2   |")
print("Метод", "{:1}|{:10.3f}|{:10.3f}|".format(1, Trapezoid(start, stop, N1), Trapezoid(start, stop, N2)))
print("Метод", "{:1}|{:10.3f}|{:10.3f}|".format(2, Bull(start, stop, N1), Bull(start, stop, N2)))
# print(trap, bul)
# print(Trapezoid(start, stop, N1))
TrapE = abs(Trapezoid(start, stop, N1) - Trapezoid(start, stop, N1 * 2))
BulE = abs(Bull(start, stop, N2) - Bull(start, stop, N2 * 2))
print("Погрешность для метода трапеций = ", TrapE)
print("Погрешность для метода Буля = ", BulE)


if TrapE > BulE:
    TrapE = 100
    print("У метода трапеций точность ниже")
    E = float(input("Введите желаемую точность для метода трапеций: "))
    N = 1
    while E < TrapE:
        N += 1
        TrapE = abs(Trapezoid(start, stop, N) - Trapezoid(start, stop, N * 2))
    print("Для метода трапеций было задано количество разделений :", N)
    print("Достигнутая точность = ", TrapE)
    print("Результат = ", Trapezoid(start, stop, N))
else:
    BulE = 100
    print("У метода Буля точность ниже")
    E = float(input("Введите желаемую точность для метода Буля: "))
    N = 1
    while E < BulE:
        N += 1
        BulE = abs(Bull(start, stop, N) - Bull(start, stop, N * 2))
    print("Для метода трапеций было задано количество разделений :", N)
    print("Достигнутая точность = ", BulE)
    print("Результат = ", Bull(start, stop, N))
