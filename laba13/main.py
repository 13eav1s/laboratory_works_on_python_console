"""
Лабораторная работа №13 “База данных в
бинарном файле”
Требуется написать программу, которая позволит с помощью меню выполнить
следующие действия по обработке базы данных, хранящейся в бинарном файле:
1. Выбрать файл для работы
2. Инициализировать базу данных
3. Вывести содержимое базы данных
4. Добавить запись в базу данных
5. Удалить запись из базы данных (по номеру в файле)
6. Поиск по одному полю
7. Поиск по двум полям
Тематика базы данных - произвольная, выбираемая на усмотрение исполнителя.
Записи должны состоять из 3-4 полей разных типов (текстовые, числовые).
Поля для поиска в пп. 5 и 6 выбираются на усмотрение исполнителя.
Примечания:
1. Записи в файле должны иметь одинаковую длину в байтах. Этого можно
достичь с помощью структур (модуль struct).
2. Удаление записи следует осуществлять без задействования новых файлов, со
сдвигом данных и сокращением размера файла при помощи метода truncate().
Краснов Леонид ИУ7-11Б
"""

# Импорт необходимых библиотек
import os.path as osp
import os
import struct


# Проверка на соответствие введенных значений полям
def input_pole_value(type_):
    #  Ввод значений полей
    if type_ == 1:
        inp = input('Введите строку (50 символов): ')
        while len(inp) == 0 or len(inp) > 50:
            inp = input('Ошибка! Введите строку (50 символов): ')
        inp = inp.encode()
    elif type_ == 2:
        inp = input('Введите целое число в диапазоне [−2 147 483 647, +2 147 483 647]: ')
        while not inp.isdigit() or int(inp) > 2147483647 or int(inp) < -2147483647:
            inp = input('Ошибка! Введите целое число в диапазоне [−2 147 483 647, +2 147 483 647]: ')
        return int(inp)
    else:
        inp = input('Введите вещественное число: ')
        inp = float(inp)
    return inp


#  Функция ввода натурального числа
def input_natural_int(text):
    inp = input(text)
    while (not inp.isdigit()) or int(inp) < 1:
        inp = input('Ошибка! Повторите попытку. ' + text)
    return int(inp)


#  Функция вывода строки-сообщения
def print_message_string(string=''):
    l = len(string)
    was = '─' * ((92 - l) // 2)
    print(was + string + '─' * (92 - len(was) - l))


#  Реализация команды help
def nav_command_help(options, params, flags):
    print('Список доступных команд: ')
    print('help')
    print('list')
    print('cd')
    print('dbset')
    print('exit')
    print('Для получения справки по команде введите [название команды] --help')


#  Реализация команды exit
def nav_command_exit(options, params, flags):
    if 'help' in flags:
        print('Введите команду exit для выхода из программы')
        return
    exit()


#  Реализация команды list
def nav_command_list(options, params, flags):
    for i in sorted(os.listdir('.'), key=lambda x: (osp.isdir(osp.join('.', x)), ord(x[0]) in range(1040, 1104)),
                    reverse=True):
        print(i)


#  Реализация команды cd
def nav_command_cd(options, params, flags):
    if 'help' in flags:
        print('Навигация по каталогам. Работает аналогично команде cd из командной строки windows')
        return
    if len(options) == 0:
        print('Ошибка! Укажите путь')
        return
    p = options[0]
    if '"' in options[0]:
        p = p[1:-1]

    #  Проверка на недопустимые символы в названии каталога
    for i in "+=[]:;«,./? \*<>|":
        if i in p:
            print('Ошибка в имени файла или каталога')
            return

    #  Проверка на существование каталога
    if not osp.isdir(osp.join('.', p)):
        print(f'Ошибка! Каталога "{p}" не существует')
        return

    os.chdir(p)


#  Реализация команды setdb
def nav_command_setdb(options, params, flags):
    if 'help' in flags:
        print('Выбирает файл базы данных для работы')
        print('Использование: dbset [название_файла]')
        print('Если в названии файла есть пробелы запишите его название так: "название файла"')
        return
    #  Проверка на ввод названия файла
    if len(options) == 0:
        print('Ошибка! Укажите файл')
        return
    f = options[0]
    if '"' in f:
        f = f[1:-1]

    # Проверка на недопустимые символы в названии
    for i in '+=[]:;«,/? \*<>|':
        if i in f:
            print('Ошибка в имени файла')
            return
    return f


#  Реализация сообщения о существовании команды
def nav_command_exception(options, params, flags):
    print(f'Error! command "{params["COMMAND_NAME"]}" not found!')


#  Парсер команд в меню навигации
def nav_parse_command(command):
    data = command.split()
    cmd = data[0]
    options = []
    params = {'COMMAND_NAME': cmd}
    flags = []
    next_param = False
    reflect = False
    for i in data[1:]:
        if reflect:
            options[-1] += ' ' + i
            if '"' in i:
                reflect = False
            continue

        if next_param:
            params[next_param] = i
            next_param = False
        if i.startswith('--'):
            flags.append(i[2:])
        elif i.startswith('-'):
            next_param = i[1:]
        elif '"' in i:
            reflect = True
            options.append(i)
        else:
            options.append(i)
    return cmd, options, params, flags


#  Вывод меню в меню редактирования бд
def edit_command_print_menu():
    print('1. Инициализировать базу данных')
    print('2. Вывести содержимое базы данных')
    print('3. Добавить запись в базу данных')
    print('4. Удалить запись из базы данных')
    print('5. Поиск по одному полю')
    print('6. Поиск по двум полям')
    print('7. Выход в меню навигации')
    print('8. Выход из программы')


def edit_command_init_db(file, format_, pole_titles):
    f = open(file, 'wb')
    f.close()


def parse_db_format(format_):
    res = map(int, format_.replace('100s', '1 ').replace('l', '2 ').replace('d', '3 ').split())
    return list(res)


#  Вывод бд
def edit_command_print_db(file, format_, pole_titles):
    if file not in os.listdir():
        print(f'Ошибка! База данных {file} не инициализирована!')
        return
    if os.path.getsize(file):
        f = open(file, 'rb')
        format_parsed = parse_db_format(format_)
        print(' ', end='')
        tmp = ('(Текстовый)', '(Целочисленный)', '(Вещественный)')
        for i in range(len(pole_titles)):
            print((pole_titles[i] + ' ' + tmp[format_parsed[i] - 1]).center(40), end='')
        print()
        BlockSize = struct.calcsize(format_)
        l = f.read(BlockSize)
        number = 1
        while l != b'':
            print(number, end='')
            data = struct.unpack(format_, l.strip())
            for i in range(len(data)):
                if format_parsed[i] == 1:
                    elem = data[i].decode().strip('\x00')
                    print(elem.center(40), end='')
                else:
                    print(str(data[i]).center(40), end='')
            print()
            number += 1
            l = f.read(BlockSize)
        f.close()
    else:
        print("Файл пуст!")
        return


#  Добавление записи
def edit_command_addline(file, format_, pole_titles):
    if file not in os.listdir():
        print(f'Ошибка! База данных {file} не инициализирована!')
        return
    f = open(file, 'rb+')
    f.seek(0, 2)
    print('Введите по порядку следующие поля:')
    for numb, title in enumerate(pole_titles):
        print(numb + 1, title)
    data_to_write = struct.pack(format_, *(input_pole_value(i) for i in parse_db_format(format_)))
    f.write(data_to_write)
    f.close()


#  Удаление записи
def edit_command_remline(file, format_, pole_titles):
    if file not in os.listdir():
        print(f'Ошибка! База данных {file} не инициализирована!')
        return
    pole_index = input_natural_int('Введите номер записи: ') - 1
    f = open(file, 'rb+')
    BlockSize = struct.calcsize(format_)
    f.seek(0, 2)
    line_amount = (f.tell()) // BlockSize

    if pole_index > line_amount - 1:
        print(f'Ошибка! Строка больше количества строк в файле ({pole_index + 1} > {line_amount})')
        return

    for i in range(pole_index, line_amount * BlockSize):
        f.seek((i + 1) * BlockSize, 0)
        replace_data = f.read(BlockSize)
        f.seek(i * BlockSize, 0)
        f.write(replace_data)

    f.seek(-BlockSize, 2)
    f.truncate()
    print(f'Строка {pole_index + 1} была удалена')
    f.close()


#  Проверка ввода
def input_pole_type_index(text, possible_strings):
    inp = input(text)
    while len(inp) == 0 or inp not in possible_strings:
        inp = input('Ошибка! ' + text)
    return possible_strings.index(inp)


#  Поиск по одному полю
def edit_command_find_1(file, format_, pole_titles):
    if file not in os.listdir():
        print(f'Ошибка! База данных {file} не инициализирована!')
        return
    f = open(file, 'rb')
    format_parsed = parse_db_format(format_)
    if len(format_parsed) == 0:
        print('Файл пустой!')
        return
    print('Поля для поиска: ')
    print(*pole_titles, sep='\n')
    find_pole_1 = input_pole_type_index('Введите поле по которому будет производиться поиск: ', pole_titles)
    find_value_1 = input_pole_value(parse_db_format(format_)[find_pole_1])

    print(' ', end='')
    tmp = ('(Текстовый)', '(Целочисленный)', '(Вещественный)')
    for i in range(len(pole_titles)):
        print((pole_titles[i] + ' ' + tmp[format_parsed[i] - 1]).center(40), end='')
    print()
    BlockSize = struct.calcsize(format_)
    l = f.read(BlockSize)
    number = 1
    while l != b'':
        data = list(struct.unpack(format_, l.strip()))
        for i in range(len(data)):
            if format_parsed[i] == 1:
                data[i] = data[i].strip(b'\x00')

        if data[find_pole_1] == find_value_1:
            print(number, end='')
            for i in range(len(data)):
                if format_parsed[i] == 1:
                    elem = data[i].decode().strip('\x00')
                    print(elem.center(40), end='')
                else:
                    print(str(data[i]).center(40), end='')
            print()
        number += 1
        l = f.read(BlockSize)

    f.close()


#  Поиск по двум полям
def edit_command_find_2(file, format_, pole_titles):
    if file not in os.listdir():
        print(f'Ошибка! База данных {file} не инициализирована!')
        return
    f = open(file, 'rb')
    format_parsed = parse_db_format(format_)
    if len(format_parsed) == 0:
        print('Файл пустой!')
        return

    print('Поля для поиска: ')
    print(*pole_titles, sep='\n')
    find_pole_1 = input_pole_type_index('Введите первое поле по которому будет производиться поиск: ', pole_titles)
    find_value_1 = input_pole_value(parse_db_format(format_)[find_pole_1])

    find_pole_2 = input_pole_type_index('Введите второе поле по которому будет производиться поиск: ', pole_titles)
    find_value_2 = input_pole_value(parse_db_format(format_)[find_pole_2])

    print(' ', end='')
    tmp = ('(Текстовый)', '(Целочисленный)', '(Вещественный)')
    for i in range(len(pole_titles)):
        print((pole_titles[i] + ' ' + tmp[format_parsed[i] - 1]).center(40), end='')
    print()
    BlockSize = struct.calcsize(format_)
    l = f.read(BlockSize)
    number = 1
    while l != b'':
        data = list(struct.unpack(format_, l.strip()))
        for i in range(len(data)):
            if format_parsed[i] == 1:
                data[i] = data[i].strip(b'\x00')

        if data[find_pole_1] == find_value_1 and data[find_pole_2] == find_value_2:
            print(number, end='')
            for i in range(len(data)):
                if format_parsed[i] == 1:
                    elem = data[i].decode().strip('\x00')
                    print(elem.center(40), end='')
                else:
                    print(str(data[i]).center(40), end='')
            print()
        number += 1
        l = f.read(BlockSize)

    f.close()


#  Выход в консоль
def edit_command_exit_to_nav(*args):
    pass


#  Выход из программы
def edit_command_exit(*args):
    exit(0)

#  Cписок функций
EDIT_COMMANDS = [
    edit_command_init_db,
    edit_command_print_db,
    edit_command_addline,
    edit_command_remline,
    edit_command_find_1,
    edit_command_find_2,
    edit_command_exit_to_nav,
    edit_command_exit
]

# Cловарь
NAV_COMMANDS = {
    'help': nav_command_help,
    'list': nav_command_list,
    'cd': nav_command_cd,
    'dbset': nav_command_setdb,
    'exit': nav_command_exit
}

edit_mode = False
FILE = None

format_ = '100s100sld'

#  Названия полей в бд
pole_titles = ['Страна-изобретатель', 'Название технологии', 'Номер заказа', 'Награда за кражу']

while True:
    if edit_mode:
        edit_command_print_menu()
        command = input_natural_int('Введите номер команды: ')
        while command > 8:
            print('Некорректный номер команды. Попробуйте снова')
            command = input_natural_int('Введите номер команды: ')
        if command == 7:
            edit_mode = False
            FILE = None
            continue
        cmd = EDIT_COMMANDS[command - 1]
        print_message_string(f'Выполнение команды {command}...')
        cmd(FILE, format_, pole_titles)
    else:
        command = input(osp.abspath(osp.curdir) + '> ')
        if len(command) == 0:
            continue
        cmd, options, params, flags = nav_parse_command(command)
        if cmd == 'dbset':
            res = NAV_COMMANDS['dbset'](options, params, flags)
            if res is None:
                continue
            FILE = res
            edit_mode = True
        NAV_COMMANDS.get(cmd, nav_command_exception)(options, params, flags)
