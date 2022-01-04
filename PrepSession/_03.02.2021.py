"""
В файле записана прямоугольная символьная матрица,
состоящая из строчных букв латинского алфавита, разделённых пробелами.
Требуется переписать в новый файл только те строки,
в которых все буквы расположены или по возрастанию позиции в алфавите, или по убыванию.
Далее требуется удалить столбцы, состоящие только из гласных букв,
и после пустой строки дописать изменённую матрицу.
"""

def matOut(matrix):
    with open("in.txt", 'a') as f:
        print("\n", file=f)
        for i in range(len(matrix)):
            flag = 0
            try:
                if matrix[i][0] == None:
                    pass
            except:
                flag = 1
            if flag != 1:
                for j in range(len(matrix[i])):
                    #  if matrix[i][j] != 0:
                    print(matrix[i][j], end=" ", file=f)
                print(file=f)
    return 0


def chekDown(string):
    for i in range(2, len(string), 2):
        lasti = i - 2
        a = findInd(string[lasti], liters)
        b = findInd(string[i], liters)
        if a < b:
            return 0
    return 1



def findInd(a, liters):
    index = None
    for i in range(len(liters)):
        if liters[i] == a:
            index = i
            break
    return index


#  строчные буквы ангилйского алфавита
liters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
          "u", "v", "w", "x", "y", "z"]
#  Гласные буквы
aliter = ["a", "e", "i", "o", "u", "y"]

matrix = []
with open("in.txt") as f:
    for i in f:
        matstring = []
        flag = 0
        for j in i:
            if flag == 0:
                lastj = j
                flag = 1
                matstring.append(lastj)
            if j != " " and flag == 2 and j != "\n":
                a = findInd(j, liters)
                b = findInd(lastj, liters)
                #  print(a, b)
                lastj = j
                if a < b:
                    crashStr = i
                    matstring.clear()
                    if chekDown(crashStr) == 1:
                        stringArr = []
                        for e in range(len(crashStr)):
                            if crashStr[e] != " " and crashStr[e] != "\n":
                                stringArr.append(crashStr[e])
                        matrix.append(stringArr)
                    break
                matstring.append(j)
            flag = 2
        if len(matstring) > 0:
            matrix.append(matstring)

#  Удаление гласных столбцов из матрицы
newMatrix = []
for i in range(len(matrix[0])):
    str = []
    for j in range(len(matrix)):
        str.append(0)
    newMatrix.append(str)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        newMatrix[j][i] = matrix[i][j]


delid = []
for i in range(len(newMatrix)):
    flag = 0
    for j in range(len(newMatrix[i]) - 1):
        if (newMatrix[i][j] in aliter) and (newMatrix[i][j + 1] in aliter):
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        delid.append(i)

delid.reverse()
for i in range(len(delid)):
    newMatrix.pop(i)
#  print(newMatrix)

matrix = []
for i in range(len(newMatrix[0])):
    str = []
    for j in range(len(newMatrix)):
        str.append(0)
    matrix.append(str)

for i in range(len(newMatrix)):
    for j in range(len(newMatrix[i])):
        matrix[j][i] = newMatrix[i][j]

#  вывод матрицы
matOut(matrix)
