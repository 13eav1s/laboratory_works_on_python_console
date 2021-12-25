"""
Найти предложение с самым большим колличеством слов
"""


def left(txt):
    for i in range(len(txt)):
        #  print(t[i])
        txt[i] = txt[i].strip()
    return txt


def findSentence(txt):
    # left(txt)
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
    colCommon = []
    colWords = []
    colWords1 = 0
    for i in range(len(sentences)):
        colWords1 = 0
        for j in range(len(sentences[i])):
            if sentences[i][j] == " " or sentences[i][j] == "." or sentences[i][j] == ",":
                sentence.append(word.copy())
                word.clear()
                colWords1 += 1
            else:
                word.append(sentences[i][j])
        colWords.append(colWords1)
        if colWords1 == max(colWords):
            colCommon.clear()
            colCommon.append(sentences[i])

    #  print(max(colWords))
    for i in range(len(colCommon)):
        a = 80
        for j in range(len(colCommon[i])):
            print(colCommon[i][j], end='')
            if j > a:
                print()
                a += 80

    # for i in range(len(sentences)):
    #     for j in range(len(sentences[i])):
    #         colWords.append(len(sentences[i][j]))
    #         print(sentences[i][j], end="")
    #     print()
    # for i in range(len(colWords)):
    #     if colWords[i] == max(colWords):
    #         print("Максимальное колличество слов в :", max(colWords))
    #         print("Индекс предложниея начиная с нуля:", i)
    #         break
    #     colWords = 0
    #     for j in range(len(sentence)):
    #         for e in range(0, len(alphabet), 2):
    #             colCommon.append(int(sentence[j].count(alphabet[e])) + int(sentence[j].count(alphabet[e + 1])))
    #             if max(colCommon) >= 2:
    #                 #  print(i, colCommon, sentence[j])
    #                 colWords += 1
    #                 colCommon = []
    #                 break
    #             colCommon = []
    #     if colWords > maxCommon:
    #         maxCommon = colWords
    #         savei = i
    #     sentence.clear()
    # print("Максимальное колличество слов с повторяющимися буквами в предложении")
    # for i in range(len(sentences[savei])):
    #     print(sentences[savei][i], end="")
    #     if i % 70 == 0:
    #         print()
    # print(".\n")


text = [
    "Вот как же так. С конца 1811-го года 5+45 началось усиленное вооружение. и сосредоточение сил Западной Европы,",
    " и в 1812 году силы эти — миллионы людей (считая тех, которые перевозили и кормили армию) ",
    "двинулись с Запада на Восток, к границам России, к которым точно так же с 1811-го года стягивались силы",
    " России. 12 июня силы Западной Европы перешли границы России, и началась война, то есть",
    " совершилось противное человеческому разуму и всей человеческой природе событие. Миллионы людей совершали",
    " друг, против друга такое бесчисленное количество злодеяний, обманов, измен,",
    " воровства, подделок. и выпуска фальшивых ассигнаций, грабежей, поджогов",
    " и убийств, которого в целые века не соберет летопись всех судов мира и на которые,",
    " в этот период времени, люди, совершавшие их, не смотрели как на преступления. как."]
findSentence(text)
