"""
Функция кос икс
Метод трапеций
Заданная точность
"""
import math as m


def F(x):
    y = x**3
    return y


def Trapezoid(A, B, N):
    e = 1e-7
    h = (B - A) / N
    x = A
    rez = 0
    while e < abs(x - (B - h)):
        rez += ((F(x) + F(x + h)) / 2) * ((x + h) - x)
        x += h
    return rez


start = float(input("Введите начало: "))
stop = float(input("Введите конец: "))
#  N = int(input("Введите N1: "))
E = float(input("Введте желаемую погрешность: "))
N = 1
x1 = Trapezoid(start, stop, N)
x2 = Trapezoid(start, stop, N * 2)
TrapE = abs(x1 - x2)
while E <= TrapE:
    N *= 2
    x1 = x2
    x2 = Trapezoid(start, stop, N * 2)
    TrapE = abs(x1 - x2)

print("Результат: ", x1)
print("N = ", N)
print("Погрешность: ", TrapE)
