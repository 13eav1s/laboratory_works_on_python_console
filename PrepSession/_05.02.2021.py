"""
В файле записан текст на английском языке, предложения разделяются точками.
Требуется переписать текст в новый файл так,
чтобы каждое предложение было записано в отдельной строке.
Более одной строки файла в память не считывать.
Далее найти предложение с наибольшим количеством слов,
в которых гласные и согласные буквы чередуются,
и дописать в файл его слова в порядке уменьшения количества букв.
"""


def fileInToFileOut():
    with open("in.txt") as f1:
        with open("out.txt", "w") as f2:
            for i in f1:
                flag = 0
                for j in i:
                    if flag == 1:
                        if j == " ":
                            print("", file=f2, end="")
                        flag = 0
                    elif j == ".":
                        flag = 1
                        print(j, file=f2, end="")
                        print(file=f2)
                    elif j == "\n":
                        print(" ", file=f2, end="")
                    else:
                        print(j, file=f2, end="")


def findWord(word):
    lit = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
    lastI = ""
    col = 0
    for i in range(len(word)):
        realCol = len(word)
        if (lastI in lit) and (not(word[i] in lit)):
            col += 1
        lastI = word[i]
        #  print(realCol, col)
        if (col == realCol // 2):
            return 1
    lastI = word[0]
    col = 0
    for i in range(len(word)):
        realCol = len(word)
        if (word[i] in lit) and (not (lastI in lit)):
            col += 1
        lastI = word[i]
        #  print(realCol, col)
        if ((col == realCol // 2) and realCol % 2 == 0) or ((col == (realCol // 2) + 1) and realCol % 2 == 1):
            return 1
    return 0


fileInToFileOut()
with open("out.txt") as f:
    maxcol = 0
    sentence = None
    for i in f:
        len_str = len(i)
        col = 0
        word = ""
        for j in range(len_str):
            if i[j] != " " and i[j] != "." and i[j] != "\n":
                word += i[j]
            else:
                if word != " " and word != "":
                    if findWord(word):
                        col += 1
                        word = ""
        if col > maxcol:
            maxcol = col
            sentence = i
with open("out.txt", "a") as f:
    print(file=f)
    print(sentence, file=f)
