"""
Лабораторная работа No7 “Списки. Часть 2”
Написать программу, которая позволит с использованием меню обеспечить
работу со строковыми массивами:
1.Очистить список и ввести его с клавиатуры
2.Добавить элемент в произвольное место списка
3.Удалить произвольный элемент из списка (по номеру)
4.Очистить список
5.Поиск элемента по варианту
6.Изменение элемента по варианту
"""


def PrintMenu():
    print("Меню: \n"
          "1. Очистить список и ввести его с клавиатуры \n"
          "2. Добавить элемент в произвольное место списка \n"
          "3. Удалить произвольный элемент из списка (по номеру) \n"
          "4. Очистить список \n"
          "5. Поиск элемента с наибольшим числом английских заглавных"
          " букв \n"
          "6. Замена всех английских заглавных букв на строчные \n")
    while True:
        elem = int(input("Введите номер пункта: "))
        if 0 <= elem <= 7:
            break
    return elem


def ClearArray(arr):
    arr.clear()
    return arr


def Fill(arr):
    number = int(input("Введите колличество элементов списка"))
    for i in range(number):
        arr.append(float(input("Введите элемент, который хотите"
                               " добавить: ")))
    return arr


def ClearAndFill(arr):
    arr = ClearArray(arr)
    arr = Fill(arr)
    print("Список выглядит так: \n", arr)
    return arr


def AddElem(arr):
    while True:
        index = int(input("Введите индекс под которым вы хотите записать"
                          " новый элемент: "))
        if index < len(arr):
            break
        else:
            print("Вы ввели индекс слишком большой индекс")
    elem = float(input("Введите элемент: "))
    arr.append(0)
    temp_elem = arr[index]
    arr[index] = elem
    for i in range(index, len(arr) - 1):
        arr[i + 1] = temp_elem
        temp_elem = arr[i]
    print("Ваш список выглядит так: \n", arr)


def RemoveElem(arr):
    print("Вы выбрали удалить произвольный элемент из списка")
    index = int(input("Введите индекс элемента, который хотите "
                      "удалить: "))
    arr2 = []
    for i in range(len(arr)):
        if i != index:
            arr2.append(arr[i])
    print("Список выглядит так: \n", arr2)
    return arr2


mass = []
item = PrintMenu()
while True:
    if item == 1:
        ClearAndFill(mass)
        item = PrintMenu()
    if item == 2:
        AddElem(mass)
        item = PrintMenu()
    if item == 3:
        RemoveElem(mass)
        item = PrintMenu()
