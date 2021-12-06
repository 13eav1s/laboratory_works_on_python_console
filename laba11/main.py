"""
Написать программу для выполнения некоторых операций с текстом. Вводить текст не
требуется, он должен быть задан в исходном тексте программы в виде списка строк
(при выводе на экран каждый элемент этого списка должен начинаться с новой
строки).
Программа должна позволять с помощью меню выполнить следующие действия:
1. Выровнять текст по левому краю
2. Выровнять текст по правому краю
3. Выровнять текст по ширине
4. Удаление всех вхождений заданного слова
5. Замена одного слова другим во всём тексте
6. Вычисление арифметических выражений внутри текста операции сложения и вычитания
7. Найти предложение, в котором количество слов, содержащих каждую букву 2 и
более раз, максимально.
В качестве текста в программе следует указать фрагмент литературного произведения
из 5-7 предложений. Текст следует разбить по строкам так, чтобы ни одна строка не
совпадала с предложением, то есть никакая строка, кроме последней, не должна
оканчиваться точкой.
"""


# Функция печатает меню
def PrintMenu():
    print("Меню: \n"
          "1. Выровнять текст по левому краю \n"
          "2. Выровнять текст по правому краю \n"
          "3. Выровнять текст по ширине \n"
          "4. Удаление всех вхождений заданного слова \n"
          "5. Замена одного слова другим во всём тексте \n"
          "6. Вычисление арифметических выражений внутри текста операции сложения и вычитания \n"
          "7. Найти предложение, в котором количество слов, содержащих каждую букву 2 и более раз, максимально. \n"
          "0. Выйти из программы \n")
    while True:
        elem = int(input("Введите номер пункта: "))
        if 0 <= elem <= 10:
            break
    return elem


#  Функция выравнивает текст по левому краю
def left(t):
    for i in range(len(t)):
        #  print(t[i])
        t[i] = t[i].strip()
    return t


def right(t):
    for i in range(len(t)):
        #  print(t[i])
        t[i] = t[i].strip()

    maxim = 0
    for i in range(len(t)):
        if len(t[i]) > maxim:
            maxim = len(t[i])
    for i in range(len(t)):
        t[i] = t[i][::-1]
        t[i] += " " * (maxim - len(t[i]))
        t[i] = t[i][::-1]
    return t


#  Функция для вывода текста
def textOut(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            print(t[i][j], end='')
        print()


def width(t):
    maxi = 0
    for i in range(len(t)):
        t[i] = t[i].strip()
        if len(t[i]) > maxi:
            maxi = len(t[i])

    for i in range(len(t)):
        t[i] = t[i].center(maxi)

    return t


def delWord(t):
    word = input("Введите слово, которое хотите удолить: ")
    for i in range(len(t)):
        t[i] = t[i].replace(word, '')
    return t


def renameWord(t):
    word = input("Введите слово, которое хотите заменить на другое: ")
    word2 = input("Введите слово, на которое вы хотите заменить")
    for i in range(len(t)):
        t[i] = t[i].replace(word, word2)
    return t


# def math(t):
#     for i in range(len(t)):
#         a = 0
#         b = 0
#         c = 0
#         start = None
#         stop = None
#         flag = 0
#         for j in range(len(t[i])):
#             if t[i][j].isdigit() and flag == 0:
#                 a = (a * 10) + int(t[i][j])
#                 start = j
#             elif t[i][j] == "+":
#                 flag = 1
#                 c = 1
#             elif t[i][j] == "-":
#                 flag = 1
#                 c = 2
#             elif t[i][j].isdigit() and flag == 1:
#                 b = (b * 10) + int(t[i][j])
#                 stop = j
#             else:
#                 break
#         if c == 1:
#             print(b + a)
#         if c == 2:
#             print(a - b)
#     return t


def arif(a):
    b = []
    for i in range(len(a)):
        line = a[i].split()
        c = ''
        b.clear()
        for k in range(len(line)):
            for j in range(len(line[k])):
                if line[k][j].isdigit():
                    c += line[k][j]
                elif len(c) > 0:
                    b.append(int(c))
                    c = ''
                if j == len(line[k])-1 and len(c) > 0:
                    b.append(int(c))
                    c = ''
                if line[k][j] == '+' or line[k][j] == '-':
                    b.append(line[k][j])
            if len(b) > 2:
                if len(b) % 2 == 1:
                    count = b[0]
                    start = 1
                else:
                    count = -b[1]
                    start = 2
                for j in range(start,len(b)-1,2):
                    if b[j] == '-':
                        count -= b[j+1]
                    elif b[j] == '+':
                        count += b[j+1]
                print(count)
                line[k] = count
            b.clear()
        a[i] = ''
        for j in range(len(line)):
            a[i] += str(line[j])+' '
    return a


# Исходный текст
"""
text = ["С конца 1811-го года 5+45 началось усиленное вооружение и сосредоточение сил Западной Европы,",
        " и в 1812 году силы эти — миллионы людей (считая тех, которые перевозили и кормили армию) ",
        "двинулись с Запада на Восток, к границам России, к которым точно так же с 1811-го года стягивались силы",
        " России. 12 июня силы Западной Европы перешли границы России, и началась война, то есть",
        " совершилось противное человеческому разуму и всей человеческой природе событие. Миллионы людей совершали",
        " друг, против друга такое бесчисленное количество злодеяний, обманов, измен,",
        " воровства, подделок и выпуска фальшивых ассигнаций, грабежей, поджогов",
        " и убийств, которого в целые века не соберет летопись всех судов мира и на которые,",
        " в этот период времени, люди, совершавшие их, не смотрели как на преступления."]
"""
text = ["23+23,",
        "asd fsa fsda + fads,",
        " dsf df 4-5 dfa dsf dsf,",
        "4 dd - 44 -as fd 10,",
        "10-15"]

# for i in range(len(text)):
#     text[i] = str(text[i][0])

# right(text)
# textOut(text)

# for i in range(len(text)):
#     for j in range(len(text[i][0])):
#         print(text[i][0][j])

# textOut(left(textOut(text)))
# for i in range(len(text)):
#     text.append(str(text[i]))

# for i in range(int(len(text) / 2)):
#     text.pop(i)

# textOut(text)

# text.split()
# for i in range(len(text)):
#     for j in range(len(text[i])):
#         text[i][j].split()
# print(text)
# textOut(text)
item = PrintMenu()
while True:
    if item == 0:
        print("Программа завершила работу")
        break
    if item == 1:
        textOut(left(text))
        item = PrintMenu()
    if item == 2:
        textOut(right(text))
        item = PrintMenu()
    if item == 3:
        textOut(width(text))
        item = PrintMenu()
    if item == 4:
        textOut(delWord(text))
        item = PrintMenu()
    if item == 5:
        textOut(renameWord(text))
        item = PrintMenu()
    if item == 6:
        textOut(math(text))
        item = PrintMenu()
print(text)
