def OutMatrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()
    print()
    return 0


a = [[3, 4, 9, 4, 6], [8, 5, 6, 6, 2], [6, 4, 5, 4, 4], [5, 3, 7, 6, 8], [4, 4, 2, 7, 4]]
OutMatrix(a)

"""
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
"""

"""Change a elements main diagonal to 0"""

for i in range(len(a)):
    a[i][i] = 0
OutMatrix(a)

"""Chenge elements under main diagonal on 123..."""

for i in range(len(a-1)):
    for j in range(len(a[i])):

