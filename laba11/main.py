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
          "8. Отключить выравнивание. \n"
          "0. Выйти из программы. \n")
    while True:
        elem = int(input("Введите номер пункта: "))
        if 0 <= elem <= 10:
            break
    return elem


#  Функция выравнивает текст по левому краю
def left(txt):
    for i in range(len(txt)):
        #  print(t[i])
        txt[i] = txt[i].strip()
    return txt


#  Функция для выравнивания текста по правой стороне
def right(txt):
    for i in range(len(txt)):
        #  print(t[i])
        txt[i] = txt[i].strip()

    maxim = 0
    for i in range(len(txt)):
        if len(txt[i]) > maxim:
            maxim = len(txt[i])
    for i in range(len(txt)):
        txt[i] = txt[i][::-1]
        txt[i] += " " * (maxim - len(txt[i]))
        txt[i] = txt[i][::-1]
    return txt


#  Функция для вывода текста
def textOut(txt):
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            print(txt[i][j], end='')
        print()


# def width(t):
#     maxi = 0
#     for i in range(len(t)):
#         t[i] = t[i].strip()
#         if len(t[i]) > maxi:
#             maxi = len(t[i])
#
#     for i in range(len(t)):
#         t[i] = t[i].center(maxi)
#
#     return t


#  Функция для удаления слова
def delWord(txt):
    word = input("Введите слово, которое хотите удолить: ")
    for i in range(len(txt)):
        txt[i] = txt[i].replace(word, '')
    return txt


#  Функция для замены слова
def renameWord(txt):
    word = input("Введите слово, которое хотите заменить на другое: ")
    word2 = input("Введите слово, на которое вы хотите заменить")
    for i in range(len(txt)):
        txt[i] = txt[i].replace(word, word2)
    return txt


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


#  Функция для нахождения предложения с налибольшим числом слов, в которых встречается любая буква больше 2-х раз
def findSentence(txt):
    alphabet = ["А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ё", "ё", "Ж", "ж", "З", "з", "И", "и",
                "Й", "й", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р", "С", "с", "Т", "т",
                "У", "у", "Ф", "ф", "Х", "х", "Ц", "ц", "Ч", "ч", "Щ", "щ", "Ъ", "ъ", "Э", "э", "Ь", "ь", "Э", "э",
                "Ю", "ю", "Я", "я", "Ы", "ы"]
    sentence = []
    sentences = []
    word = []
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            if txt[i][j] == '.':
                sentences.append(sentence.copy())
                #  print(sentence)
                sentence.clear()
            else:
                sentence.append(txt[i][j])
    #  print(sentences)
    #  del sentence
    sentence = []
    savei = 0
    maxCommon = 0
    colCommon = []
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            if sentences[i][j] == " " or sentences[i][j] == "." or sentences[i][j] == ",":
                sentence.append(word.copy())
                word.clear()
            else:
                word.append(sentences[i][j])

        colWords = 0
        for j in range(len(sentence)):
            for e in range(0, len(alphabet), 2):
                colCommon.append(int(sentence[j].count(alphabet[e])) + int(sentence[j].count(alphabet[e + 1])))
                if max(colCommon) >= 2:
                    print(i, colCommon, sentence[j])
                    colWords += 1
                    colCommon = []
                    break
                colCommon = []
        if colWords > maxCommon:
            maxCommon = colWords
            savei = i
        sentence.clear()
    print("Максимальное колличество слов с повторяющимися буквами в предложении")
    for i in range(len(sentences[savei])):
        print(sentences[savei][i], end="")
        if i % 70 == 0:
            print()
    print(".\n")


#  Функция выполняет арифметические операции в тексте
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
                if j == len(line[k]) - 1 and len(c) > 0:
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
                for j in range(start, len(b) - 1, 2):
                    if b[j] == '-':
                        count -= b[j + 1]
                    elif b[j] == '+':
                        count += b[j + 1]
                print(count)
                line[k] = count
            b.clear()
        a[i] = ''
        for j in range(len(line)):
            a[i] += str(line[j]) + ' '
    return a


# Исходный текст

text = ["Вот как же так. С конца 1811-го года 5+45 началось усиленное вооружение. и сосредоточение сил Западной Европы,",
        " и в 1812 году силы эти — миллионы людей (считая тех, которые перевозили и кормили армию) ",
        "двинулись с Запада на Восток, к границам России, к которым точно так же с 1811-го года стягивались силы",
        " России. 12 июня силы Западной Европы перешли границы России, и началась война, то есть",
        " совершилось противное человеческому разуму и всей человеческой природе событие. Миллионы людей совершали",
        " друг, против друга такое бесчисленное количество злодеяний, обманов, измен,",
        " воровства, подделок и выпуска фальшивых ассигнаций, грабежей, поджогов",
        " и убийств, которого в целые века не соберет летопись всех судов мира и на которые,",
        " в этот период времени, люди, совершавшие их, не смотрели как на преступления. как."]
t = text.copy()


# Функция выравнивания списка строк по ширине
def width_alig(li):
    li[0] = li[0].strip()
    max_row_len = len(li[0])
    for i in range(1, len(li)):
        li[i] = li[i].strip()
        if len(li[i]) > max_row_len:
            max_row_len = len(li[i])
    for i in range(len(li)):
        while len(li[i]) != max_row_len:
            for j in range(len(li[i])):
                if len(li[i]) != max_row_len:
                    if li[i][j] == " ":
                        li[i] = li[i][:j + 1] + "$" + li[i][j + 1:]
        li[i] = li[i].replace("$", " ")
    return li


# Функция для отключения выравнивания (Уже не используется)
def off_width(txt):
    for i in range(len(txt) - 1):
        if txt[i] == " " and txt[i + 1] == " ":
            txt[i + 1] = ""
    return txt


# text = ["23+23,",
#         "asd fsa + fads,",
#         " dsf df 4-5 dfa dsf dsf,",
#         "4 dd - 44 -as fd 10,",
#         "10-15"]

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
''''''

#  точка входа в программу

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
        textOut(width_alig(text))
        item = PrintMenu()
    if item == 4:
        textOut(delWord(text))
        item = PrintMenu()
    if item == 5:
        textOut(renameWord(text))
        item = PrintMenu()
    if item == 6:
        textOut(arif(text))
        item = PrintMenu()
    if item == 7:
        findSentence(text)
        item = PrintMenu()
    if item == 8:
        text = t.copy()
        print("Отключены все выравнивания")
        item = PrintMenu()
print(text)
