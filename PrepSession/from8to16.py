"""
В файле in.txt записаны дробные числа в 8-ричной системе счисления, по одному в строке, разделитель целой и дробной
части - точка.
Требуется:
1. Перевести числа из исходного файла в 16-ричную систему счисления и переписать их в файл out1.txt по одному в строке
в том же порядке.
2. Переписать строки файла out1.txt в файл out2.txt, отсортировав их по увеличению длин.
Обработку файлов производить построчно, содержимое файла читать в память целиком запрещается. Списки, множества,
словари, кортежи для сортировки не использовать.
"""


def transformto10(num, step):
    numf = float(num)
    numi = int(numf)
    # i = numi % 10
    i = 0
    if "." in num:
        while num[i] != ".":
            i += 1
        i -= 1
    else:
        i = len(num)
    #  print(numi, i)
    tennum = 0
    for j in range(len(num)):
        if num[j] != ".":
            tennum = tennum + (int(num[j]) * 8 ** i)
            i -= 1
    return tennum


def transformto16(num):
    #  print(num)
    num = str(num)
    savenum = num
    beforpoint = ""
    #  print(num)
    i = 0
    if "." in num:
        while savenum[i] != '.':
            beforpoint += savenum[i]
            #  num = num.replace(num[i], "")
            i += 1
        beforpoint += savenum[i]
        #  print(beforpoint, num)
    else:
        beforpoint = savenum
        num = "0.0"
    if num != "0.0":
        num ="0." + num.replace(beforpoint, "")
    else:
        num = 0
    rem = float(num)
    #  print(num)
    beforpoint = float(beforpoint)
    beforpoint = int(beforpoint)
    step = 16
    #  print(beforpoint)
    rems = []
    liters = {
        "0" : "0",
        '1' : '1',
        '2' : '2',
        '3' : '3',
        '4' : '4',
        '5' : '5',
        '6' : '6',
        '7' : '7',
        '8' : '8',
        '9' : '9',
        '10' : "A",
        '11' : "B",
        '12' : "C",
        '13' : "D",
        '14' : "E",
        '15' : "F",
    }
    while beforpoint >= step:
        rems.append(beforpoint % step)
        beforpoint //= step
    rems.append(beforpoint % step)
    rems.reverse()
    beforpoint = ""
    for i in range(len(rems)):
        beforpoint += liters[str(rems[i])]
    #  print(beforpoint, rems)

    rems = []
    while rem > 0:
        torems = rem * 16
        rem = int(torems)
        rems.append(rem)
        rem = torems - rem
    #  print(rems)

    afterpoint = ""
    for i in range(len(rems)):
        afterpoint += liters[str(rems[i])]
    if afterpoint != "":
        rez = beforpoint + "." + afterpoint
        #  print(rez)
        return rez
    else:
        return beforpoint


with open("in.txt") as f:
    with open("out.txt", "w") as f2:
        for i in f:
            num = i
            num = num.replace("\n", "")
            num10 = transformto10(num, 8)
            rez = transformto16(num10)
            print(rez, file=f2)

