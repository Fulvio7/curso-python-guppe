"""
7- Gerar uma matriz 10x10, onde seus elementos são da forma:
-> A[i][j] = 2i + 7j, se i < j
-> A[i][j] = 3i² - 1, se i = j
-> A[i][j] = 4i³ - 5j², se i > j
"""

matriz = [[], [], [], [], [], [], [], [], [], []]

for i in range(10):
    for j in range(10):
        if i < j:
            matriz[i].append((2*i)+(5*j))
        elif i == j:
            matriz[i].append((3*(i**2))-1)
        else:
            matriz[i].append((4*(i**3))-(5*(j**2)))

for i in range(10):
    for j in range(10):
        print(matriz[i][j], end='  ')
    print('')











