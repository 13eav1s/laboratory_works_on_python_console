"""
Создать текст файл
чтать строки и реверсировать четные
строки и записывать в новый файл
"""


with open("in.txt") as f1:
    i = 0
    while True:
        i += 1
        str = f1.readline().strip()
        if str == "":
            break
        with open("out.txt", "a") as f2:
            if i % 2:
                str2 = ""
                for j in range(len(str)):
                    str2 += str[len(str) - j - 1]
                f2.write(str2)
                f2.write("\n")
            else:
                f2.write(str)
                f2.write("\n")


#  with open("in.txt") as in1, open("out.txt"):

