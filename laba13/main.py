# """
# Лабораторная работа №13 “База данных в
# бинарном файле”
# Требуется написать программу, которая позволит с помощью меню выполнить
# следующие действия по обработке базы данных, хранящейся в бинарном файле:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных
# 3. Вывести содержимое базы данных
# 4. Добавить запись в базу данных
# 5. Удалить запись из базы данных (по номеру в файле)
# 6. Поиск по одному полю
# 7. Поиск по двум полям
# Тематика базы данных - произвольная, выбираемая на усмотрение исполнителя.
# Записи должны состоять из 3-4 полей разных типов (текстовые, числовые).
# Поля для поиска в пп. 5 и 6 выбираются на усмотрение исполнителя.
# Примечания:
# 1. Записи в файле должны иметь одинаковую длину в байтах. Этого можно
# достичь с помощью структур (модуль struct).
# 2. Удаление записи следует осуществлять без задействования новых файлов, со
# сдвигом данных и сокращением размера файла при помощи метода truncate().
#
# Краснов Леонид ИУ7-11Б
# """
#
#
# def printMenu():  # Функция печатает меню
#     print("Меню: \n"
#           "1. Выбрать файл для работы \n"
#           "2. Инициализировать базу данных \n"
#           "3. Вывести содержимое базы данных \n"
#           "4. Добавить запись в базу данных \n"
#           "5. Удалить запись из базы данных (по номеру в файле) \n"
#           "6. Поиск по одному полю \n"
#           "7. Поиск по двум полям \n"
#           "0. Выйти из программы \n")
#     while True:
#         try:
#             elem = int(input("Введите номер пункта: "))
#             if 0 <= elem <= 7:
#                 break
#         except:
#             pass
#     return elem
#
#
# # Функция выбора файла
# def file_choice(file_name):
#     try:
#         f = open(file_name, "a")
#     except FileNotFoundError:
#         print("\nТакого файла нет")
#         return ""
#     except OSError:
#         print("\nНеверный синтаксис поиска файла")
#         return ""
#     else:
#         f.close()
#         return file_name
#
#
# # Функция создания файла
# def file_creature(file_name):
#     try:
#         f = open(file_name, "w")
#     except OSError:
#         print("\nНеверный синтаксис создания файла")
#         return ""
#     else:
#         f.close()
#         return file_name
#
#
# # Функция инициализации базы данных
# def database_init(file_name):
#     while True:
#         if not file_name:
#             print("\nФайл ещё не выбран. Создайте новый файл")
#             new_file_name = input("\nСоздайте файл для работы: ")
#             new_file_name = file_creature(new_file_name)
#             if new_file_name:
#                 return new_file_name
#         else:
#             new_file_name = file_creature(file_name)
#             print("\nФайл был перезаписан")
#             if new_file_name:
#                 return new_file_name
#
#
# # Вывод базы данных
# def print_database(db_name):
#     if db_name:
#         print("\n", "-" * 79, sep="")
#         print("|{:^77s}|".format("<Блюда>"))
#         print("-" * 79)
#         print("|{:<25s}|{:<25s}|{:<25s}|".format("Страна изобретатель", "Название", "Цена за 100 грамм"))
#         print("-" * 79)
#         with open(db_name) as db:
#             for line in db:
#                 print(line, end="")
#         print("-" * 79)
#     else:
#         print("\nБаза данных не инициализированна")
#
#
# def newFile():
#     name = input("Введите имя файла: ")
#     open(name, 'w')
#
#
# item = printMenu()
# file = ""
# database = ""
# while True:
#     if item == 0:
#         print("Программа завершила работу")
#         break
#     if item == 1:
#         file = input("\nВыберите файл для работы: ")
#         file_choice(file)
#         item = printMenu()
#     if item == 2:
#         database_init(file)
#         item = printMenu()
#     if item == 3:
#         print_database(database)
#         item = printMenu()
#     if item == 4:
#         pass
#         item = printMenu()
#     if item == 5:
#         pass
#         item = printMenu()
#     if item == 6:
#         pass
#         item = printMenu()
#     if item == 7:
#         pass
#         item = printMenu()
#
# a = bytearray("Hi".encode("UTF-8"))
# print(len(a))
# print(a)


with open("data.bin", "rb") as f:
    #  b = 100
    b = f.read()
    print(b)
