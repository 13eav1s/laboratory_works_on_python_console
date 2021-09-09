def outmatrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()
    print()
    return 0


a = [[3, 4, 9, 4, 6], [8, 5, 6, 6, 2], [6, 4, 5, 4, 4], [5, 3, 7, 6, 8], [4, 4, 2, 7, 4]]
outmatrix(a)

"""
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
"""
for i in range(len(a)):
    a[i][i] = 0
outmatrix(a)
