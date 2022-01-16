"""
Дан текстовый файл in.txt, содержащий строки.
Часть строк содержит в себе простые арифметические выражения
из одного действия над целыми числами.
Допустимые действия - сложение, вычитание, умножение, деление (деление на 0 отсутствует).
Пример строки: "экзамен 10 + 2 числа".
Переписать содержимое исходного файла в файл out.txt по следующему правилу:
если следующая строка содержит арифметическое выражение, то текущую строку переписать N раз,
где N - значение выражения, в противном случае - переписать текущую строку 1 раз.
"""

def mathematic(str):
    lenth = len(str)
    dig1 = 0
    dig2 = 0
    flag = 0
    znak = 0
    for i in range(lenth):
        if str[i].isdigit() and flag == 0:
            while str[i] != " " and str[i] != ".":
                dig1 = dig1*10 + int(str[i])
                i += 1
                flag = 1
        if str[i] == "+" or str[i] == "-" or str[i] == "*" or str[i] == "/":
            if str[i] == "+":
                znak = 1
            elif str[i] == "-":
                znak = 2
            elif str[i] == "*":
                znak = 3
            elif str[i] == "/":
                znak = 4
            flag = 2
        if str[i].isdigit() and flag == 2 and str[i] != ".":
            while str[i] != " " and str[i] != ".":
                dig2 = dig2*10 + int(str[i])
                i += 1
            flag = 3
        if flag == 3:
            if znak == 1:
                return dig1 + dig2
            elif znak == 2:
                return dig1 - dig2
            elif znak == 3:
                return dig1 * dig2
            elif znak == 4:
                return dig1 // dig2
    return 1


with open("in.txt") as f:
    with open("out.txt", "w") as f2:
        for i in f:
            col = mathematic(i)
            for j in range(col):
                if i[len(i) - 1] == "\n":
                    print(i, file=f2, end="")
                else:
                    print(i, file=f2)
