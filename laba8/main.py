"""
Написать программу, которая позволит с использованием меню обеспечить работу с
целочисленными матрицами:
1. Ввести матрицу
2. Добавить строку
3. Удалить строку
4. Добавить столбец
5. Удалить столбец
6. Найти строку, имеющую определённое свойство по варианту
7. Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов
8. Найти столбец, имеющий определённое свойство по варианту
9. Переставить местами столбцы с максимальной и минимальной суммой
элементов
10. Вывести текущую матрицу
"""


def PrintMenu():
    print("Меню: \n"
          "1. Ввести матрицу \n"
          "2. Добавить строку \n"
          "3. Удалить произвольный элемент из списка (по номеру) \n"
          "4. Очистить список \n"
          "5. Поиск элемента с наибольшим числом английских заглавных"
          " букв \n"
          "6. Замена всех английских заглавных букв на строчные \n"
          "0. Выйти из программы")
    while True:
        elem = int(input("Введите номер пункта: "))
        if 0 <= elem <= 7:
            break
    return elem