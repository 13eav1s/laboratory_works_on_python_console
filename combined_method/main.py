from matplotlib import pyplot as plt
from math import *


def f(x, func):
    return eval(func)


def derivative1(x, dx, func):
    return (f(x + dx, func) - f(x, func)) / dx


def derivative2(x, dx, func):
    return (derivative1(x + dx, dx, func) - derivative1(x, dx, func)) / dx


def main():
    dx = 0.00001
    func = str(input("Введите функцию: "))
    a = float(input("Введите начало отрезка: "))
    b = float(input("Введите конец отрезка: "))
    h = float(input("Введите шаг: "))
    eps = float(input("Введите допустимую погрешность: "))
    x1 = a
    x2 = a + h
    flag = 0
    while x2 <= b:
        if f(x1, func) * derivative2(x1, dx, func) > 0 > f(x2, func) * derivative2(x2, dx, func):
            while abs(x1 - x2) >= eps:
                newx1 = x1 - (f(x1, func) / derivative1(x1, dx, func))
                newx2 = x2 - ((x1 - x2) / (f(x1, func) - f(x2, func))) * f(x2, func)
                x1 = newx1
                x2 = newx2
            print((x1 + x2) / 2)
            flag = 1
        elif f(x1, func) * derivative2(x1, dx, func) < 0 < f(x2, func) * derivative2(x2, dx, func):
            while abs(x1 - x2) >= eps:
                newx1 = x2 - ((x1 - x2) / (f(x1, func) - f(x2, func))) * f(x2, func)
                newx2 = x1 - (f(x1, func) / derivative1(x1, dx, func))
                x1 = newx1
                x2 = newx2
            print((x1 + x2) / 2)
            flag = 1
        else:
            print("На отрезке больше одного корня или корней нет")
        x1 = x2
        x2 += h
    if flag == 0:
        print("Нет корней на введенном вами интервале")

    graph = plt
    i = -10
    step = 0.001
    x = []
    y = []
    while i <= 10:
        x.append(i)
        y.append(f(i, func))
        i += step
    graph.plot(x, y)
    graph.show()


if __name__ == "__main__":
    main()
