"""
Лабораторная работа №6 “Списки”
Написать программу, которая позволит с использованием меню обеспечить
работу с числовыми массивами:
1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда
2. Очистить список и ввести его с клавиатуры
3. Добавить элемент в произвольное место списка
4. Удалить произвольный элемент из списка (по номеру)
5. Очистить список
6. Найти значение K-го экстремума в списке
7. Найти наиболее длинную последовательность по варианту
Требуется реализовать “защиту от дурака” - проверки ввода числовых
значений на корректность без использования исключений, только с помощью
доступных операций со строками.
Вариант № 8
Краснов Леонид ИУ7-11Б
Знакочередующаяся последовательность чётных чисел
Примечания:
1. Экстремум - максимальное или минимальное значение. В рамках данной
задачи считать экстремумом значение в списке, которое больше либо меньше
одновременно двух соседних элементов.
2. Использование меню предполагает, что пользователь может самостоятельно
и многократно выбирать, какой из функций, заложенных в программе, ему
воспользоваться. Это означает, что пронумерованный список всех действий
должен быть выведен на экран в виде меню, а также должно быть оформлено
приглашение ввода, предлагающее пользователю выбрать какой-либо пункт.
После выполнения действия снова должно отображаться меню и приглашение
ввода. Можно выводить меню не после каждого действия, а через 3-5
действий, но так, чтобы оно не пропадало за границы экрана.
3. В лабораторной работе можно создавать пользовательские функции, но в
случае их использования необходимо уметь объяснить понятие подпрограммы,
принцип работы и назначение созданных функций.
"""

import math as m


# Функция проверяет введенное значение на то что оно является
# целочисленным, и если это так, то возваращает его

def Check_Input_Is_Number(value1, value2):
    while True:
        point = 0
        minus = 0
        number = input(value1)
        e = 0
        for i in range(len(number)):
            if ord("0") <= ord(number[i]) <= ord("9") or\
                    (number[i] == "." and i == 1 and point == 0) or\
                    (number[i] == "-" and i == 0) or\
                    (number[i] == "." and i == 2 and
                     number[0] == "-" and point == 0) or\
                    (number[i] == "." and i == 1 and number[0] == "0") or\
                    (number[i] == "." and i == 2 and number[0] == "-" and
                     number[1] == "0") or (number[i] == "."):
                e = 1
                if number[i] == ".":
                    point += 1
                if number[i] == "-":
                    minus += 1
            else:
                e = 0
                break
            if minus > 1 or point > 1:
                e = 0
                break
        if e == 1:
            break
        print(value2)
    return float(number)


def Check_Input_Is_Int(value1, value2):
    while True:
        menu = input(value1)
        e = 0
        for i in range(len(menu)):
            if ord("0") <= ord(menu[i]) <= ord("9"):
                e = 1
            else:
                e = 0
                break
        if e == 1:
            break
        print(value2)
    return int(menu)


def PrintMenu():
    print("Меню : \n"
          "1. Проинициализировать список первыми N элементами заданного"
          "в л/р 5 ряда \n"
          "2. Очистить список и ввести его с клавиатуры \n"
          "3. Добавить элемент в произвольное место списка \n"
          "4. Удалить произвольный элемент из списка (по номеру) \n"
          "5. Очистить список \n"
          "6. Найти значение K-го экстремума в списке \n"
          "7. Найти наиболее длинную последовательность по варианту \n"
          "0. Выйти из программы \n")
    value1 = "Введите номер пункта меню (целое число от 1 до 7) :"
    value2 = "Вы ввели несуществующий пункт. Пункт меню - целое число!"
    while True:
        menu = Check_Input_Is_Int(value1, value2)
        if 0 <= menu <= 7:
            break
    return menu


# Функция из меню пункт 1
def Action1(ArrayFunc):
    print("Вы выбрали Проинициализировать список первыми N элементами "
          "заданного в л/р 5 ряда")
    N = Check_Input_Is_Int("Введите колличество элементов массива: ",
                           "Введите целое число")
    for i in range(N):
        ArrayFunc.append((2 * i - 1)/(m.sqrt(2)**i))
    print("Ряд был проинициализарован сейчас он выглядит так: \n",
          ArrayFunc)
    return ArrayFunc


# Функция из меню пункт 2
def Action2(ArrayFunc):
    print("Вы выбрали очистить список и ввести его с клавиатуры")
    ArrayFunc.clear()
    N = Check_Input_Is_Int("Введите колличество элементов массива: ",
                           "Введите целое число")
    for i in range(N):
        ArrayFunc.append(Check_Input_Is_Number("Введите элемент массива",
                                               "Программа работаеат с "
                                               "чиловыми массивами!"))
    print("Ряд был введен сейчас он выглядит так: \n",
          ArrayFunc)
    return ArrayFunc


def Action3(ArrayFunc):
    if len(ArrayFunc) == 0:
        print("Список пуст, добавьте в него элементы!")
        return ArrayFunc
    N = Check_Input_Is_Number("Введите элемент, который хотите добавить:"
                              " ", "Элемент должен быть числом!")
    while True:
        index = Check_Input_Is_Int("Введите индекс элемента, который "
                                   "хотите поменять: ", "Индекс - это "
                                                        "целое число!")
        if len(ArrayFunc) > index:
            break
    ArrayFunc.insert(index, N)
    print("Так выглядит список сейчас: ", ArrayFunc)
    return ArrayFunc


def Action4(ArrayFunc):
    print("Вы выбрали пункт: удалить произвольный элемент")
    while True:
        index = Check_Input_Is_Int("Введите индекс элемента: ",
                                   "Индекс - это целое число!")
        if index < len(ArrayFunc):
            break
    ArrayFunc.remove(index)
    print("Список на настоящий момент: \n", ArrayFunc)
    return ArrayFunc


def Action5(ArrayFunc):
    print("Вы выбрали пункт: очистить список! ")
    ArrayFunc.clear()
    print("Теперь список пуст!")
    return ArrayFunc


def Action6(ArrayFunc):
    print("Вы выбрали пункт: найти K-ый экстремиум")
    while True:
        K = Check_Input_Is_Int("Введите номер экстремиума: ",
                               "Номер - это целое число!")


array = []
action = PrintMenu()
while True:
    if action == 1:
        array = Action1(array)
        action = PrintMenu()
    if action == 2:
        array = Action2(array)
        action = PrintMenu()
    if action == 3:
        array = Action3(array)
        action = PrintMenu()
    if action == 4:
        array = Action4(array)
        action = PrintMenu()
    if action == 5:
        array = Action5(array)
        action = PrintMenu()
    if action == 0:
        break
    if action > 5:
        print("Пункты пока еще не реализованы!")
        action = PrintMenu()
