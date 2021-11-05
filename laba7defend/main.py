"""
Произвольный список, вывести слово с наибольшем колличеством заглавных английских букв
"""


# Функция очищает список
def ClearArray(arr):
    arr.clear()
    return arr


# Функция для заполнения списка элементами
def Fill(arr):
    number = int(input("Введите колличество элементов списка: "))
    for i in range(number):
        arr.append(input("Введите элемент, который хотите"
                         " добавить: "))
    return arr


# Функция состоит из двух функций - очистки списка и записи в
# него новых элементов
def ClearAndFill(arr):
    print("Вы выбрали очистить список и ввести новые элементы: \n")
    arr = ClearArray(arr)
    arr = Fill(arr)
    print("Список выглядит так: \n", arr)
    return arr


def FiElVBiSi(arr):
    MaximeIndex = len(arr)
    MaxElem = 0
    LastMax = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if ord("A") <= ord(arr[i][j]) <= ord("Z"):
                MaxElem += 1
        if MaxElem >= LastMax:
            LastMax = MaxElem
            MaximeIndex = i
        MaxElem = 0
    if MaximeIndex < len(arr):
        print("Элемент с наибольшем колличеством заглавных букв: \n",
              arr[MaximeIndex])
    return arr


spisok = []
ClearAndFill(spisok)
FiElVBiSi(spisok)
