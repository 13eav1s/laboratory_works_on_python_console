"""
Лабораторная работа №12 база данных в текстовом фойле
Краснов Леонид ИУ7-11Б
Действия программы
1. Выбрать файл для работы
2. Инициализировать базу данных
3. Вывести содержимое из базы данных
4. Добавить запись в базу данных
5. Поиск по одному полю
6. Поиск по двум полям
"""


# Функция печатает меню
def PrintMenu():
    print("Меню: \n"
          "1. Выбрать файл для работы \n"
          "2. Инициализировать базу данных \n"
          "3. Вывести содержимое из базы данных \n"
          "4. Добавить запись в базу данных \n"
          "5. Поиск по одному полю \n"
          "6. Поиск по двум полям \n"
          "0. Выйти из программы. \n")
    while True:
        try:
            elem = int(input("Введите номер пункта: "))
            if 0 <= elem <= 10:
                break
        except ValueError or UnboundLocalError:
            pass
    return elem


#  Функция для выбора файла для работы
# def chooseFile():
#     filePath = input("Введите путь файла, который хотите выбрать")
#     return filePath


# def NewDB(path):
#     try:
#         with open(path) as file:
#             pass
#     except:


# Функция вызова меню
# def menu():
#     print("\n1. Выбрать файл для работы")
#     print("2. Инициализировать базу данных")
#     print("3. Вывести содержимое базы данных")
#     print("4. Добавить запись в базу данных")
#     print("5. Поиск по одному полю")
#     print("6. Поиск по двум полям")
#     print("0. Выход из программы\n")


# Функция выбора файла
def file_choice(file_name):
    try:
        f = open(file_name, "a")
    except FileNotFoundError:
        print("\nТакого файла нет")
        return ""
    except OSError:
        print("\nНеверный синтаксис поиска файла")
        return ""
    else:
        f.close()
        return file_name


# Функция создания файла
def file_creature(file_name):
    try:
        f = open(file_name, "w")
    except OSError:
        print("\nНеверный синтаксис создания файла")
        return ""
    else:
        f.close()
        return file_name


# Функция инициализации базы данных
def database_init(file_name):
    while True:
        if not file_name:
            print("\nФайл ещё не выбран. Создайте новый файл")
            new_file_name = input("\nСоздайте файл для работы: ")
            new_file_name = file_creature(new_file_name)
            if new_file_name:
                return new_file_name
        else:
            new_file_name = file_creature(file_name)
            print("\nФайл был перезаписан")
            if new_file_name:
                return new_file_name


# Вывод базы данных
def print_database(db_name):
    if db_name:
        print("\n", "-" * 79, sep="")
        print("|{:^77s}|".format("<Блюда>"))
        print("-" * 79)
        print("|{:<25s}|{:<25s}|{:<25s}|".format("Страна изобретатель", "Название", "Цена за 100 грамм"))
        print("-" * 79)
        with open(db_name) as db:
            for line in db:
                print(line, end="")
        print("-" * 79)
    else:
        print("\nБаза данных не инициализированна")


def newFile():
    name = input("Введите имя файла: ")
    open(name, 'w')


# Функция добавления записи в базу данных
def add_record(db_name):
    if db_name:
        with open(db_name, "a") as db:
            while True:
                print("\nВведите страну, в которой впервые появилось блюдо: ", end="")
                field1 = input()
                if not field1:
                    print("\nНеверный ввод")
                else:
                    db.write("|" + field1 + " " * (25 - len(field1)))
                    break
            while True:
                print("Введите название блюда: ", end="")
                field2 = input()
                if not field2:
                    print("\nНеверный ввод")
                else:
                    db.write("|" + field2 + " " * (25 - len(field2)))
                    break
            while True:
                print("Введите цену за 100 грамм еды : ", end="")
                field3 = input()
                if not field3.isdigit():
                    print("\nНеверный ввод")
                else:
                    db.write("|" + field3 + " " * (25 - len(field3)) + "|" + "\n")
                    break
    else:
        print("\nБаза данных не инициализированна")


# Функция поиска по одному полю
def search_by_one_field(db_name):
    if db_name:
        field_for_search = input("\nВведите значение поля: ")
        print("\n", "-" * 79, sep="")
        print("|{:^77s}|".format("Блюда"))
        print("-" * 79)
        print("|{:<25s}|{:<25s}|{:<25s}|".format("Страна изобретатель", "Название", "Цена за 100 грамм"))
        print("-" * 79)
        with open(db_name) as db:
            for line in db:
                if "|" + field_for_search + " " in line or "|" + field_for_search + "|" in line:
                    print(line, end="")
        print("-" * 79)
    else:
        print("\nБаза данных не инициализированна")


# Функция поиска по одному полю
def search_by_two_field(db_name):
    if db_name:
        field_for_search1 = input("\nВведите значение 1-го поля: ")
        field_for_search2 = input("Введите значение 2-го поля: ")
        print("\n", "-" * 79, sep="")
        print("|{:^77s}|".format("Блюда"))
        print("-" * 79)
        print("|{:<25s}|{:<25s}|{:<25s}|".format("Страна изобретатель", "Название", "Цена за 100 грамм"))
        print("-" * 79)
        with open(db_name) as db:
            for line in db:
                if ("|" + field_for_search1 + " " in line or "|" + field_for_search1 + "|" in line) and \
                        ("|" + field_for_search2 + " " in line or "|" + field_for_search2 + "|" in line):
                    print(line, end="")
        print("-" * 79)
    else:
        print("\nБаза данных не инициализированна")


# # Основная функция программы
# def main():
#     file = ""
#     database = ""
#     while True:
#         menu()
#         choice = input("Выберите пункт меню: ")
#         if choice == "0":
#             break
#         elif choice == "1":
#             file = input("\nВыберите файл для работы: ")
#             file = file_choice(file)
#             database = file
#         elif choice == "2":
#             database = database_init(file)
#         elif choice == "3":
#             print_database(database)
#         elif choice == "4":
#             add_record(database)
#         elif choice == "5":
#             search_by_one_field(database)
#         elif choice == "6":
#             search_by_two_field(database)
#         else:
#             print("\nНеверный ввод")


#  точка входа в программу
item = PrintMenu()
file = ""
database = ""
while True:
    if item == 0:
        print("Программа завершила работу")
        break
    elif item == 1:
        file = input("\nВыберите файл для работы: ")
        file = file_choice(file)
        database = file
        item = PrintMenu()
    elif item == 2:
        database = database_init(file)
        item = PrintMenu()
    elif item == 3:
        print_database(database)
        item = PrintMenu()
    elif item == 4:
        add_record(database)
        item = PrintMenu()
    elif item == 5:
        search_by_one_field(database)
        item = PrintMenu()
    elif item == 6:
        search_by_two_field(database)
        item = PrintMenu()
    elif item == 7:
        newFile()
        item = PrintMenu()
    else:
        print("\nНеверный ввод")

