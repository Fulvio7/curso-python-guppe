"""
37- Considere um vetor A com 11 elementos, ordene-o da forma a seguir:
A0 < A1 < A2 < A3 < A4 < A5 > A6 > A7 > A8 > A9 > A10
Onde A5 é o maior elemento.
"""

a = []  # [10, 3, 6, 7, 4, 1, 8, 9, 0, 2, 5]
print('Digite 11 números inteiros diferentes')
for i in range(11):
    if i == 0:
        a.append(int(input('A[0] = ')))
        n = a[0]
    else:
        while n in a:
            n = int(input(f'A[{i}] = '))
        a.append(n)

a.sort()
print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5, 8):
    a[i], a[15-i] = a[15-i], a[i]

print(a)  # [0, 1, 2, 3, 4, 10, 9, 8, 7, 6, 5]






