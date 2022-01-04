"""
В файле записаны строки, состоящие из звёздочек и пробелов.
Требуется сформировать числовую матрицу по следующему правилу:
количество строк соответствует количеству строк в файле,
а значения элементов показывают количество подряд идущих звёздочек в строке.
В случае, если строки матрицы получаются разной длины,
дополнить более короткие строки нулями до длины максимальной строки.
Вывести в новый файл полученную матрицу.
Затем отсортировать столбцы матрицы по возрастанию суммы их элементов и
дописать изменённую матрицу в выходной файл после пустой строки.
"""

with open("in.txt") as f:
    colStr = 0
    matrix = []
    for i in f:
        strsize = len(i)
        colStr += 1
        num = 0
        matstr = []
        flag = 0
        for j in range(1, strsize):
            if i[j] == i[j - 1]:
                num += 1
                flag = 0
            else:
                matstr.append(num + 1)
                num = 0
                flag = 1
        if flag == 0:
            matstr.append(num + 1)
            matrix.append(matstr)
        else:
            matrix.append(matstr)
print("Количество строк в матрице:", colStr)

#  Поиск максимальной длины строки матрицы
maxlen = 0
for i in range(len(matrix)):
    if maxlen < len(matrix[i]):
        maxlen = len(matrix[i])
#  Заполнение матрицы недостоющими нулями
for i in range(len(matrix)):
    for j in range (maxlen - len(matrix[i])):
        matrix[i].append(0)

#  Вывод матрицы в файл
with open("out.txt", "w") as f:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="", file=f)
        print(file=f)
