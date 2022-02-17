"""
В одномерном массиве удалить (алгоритмически) повторные вхождения элементов. Нельзя использовать del, remove, pop.
Срезы можно использовать только 1 раз.
"""

mass = []
size = int(input("Введите размер массива: "))
for i in range(size):
    mass.append(input("Введите элемент массива: "))
finishMass = []
for i in range(size):
    if mass[i] in finishMass:
        pass
    else:
        finishMass.append(mass[i])
    # if flag == 0:
    #     finishMass.append(mass[i])
for i in range(len(finishMass)):
    print(finishMass[i], end=" ")
