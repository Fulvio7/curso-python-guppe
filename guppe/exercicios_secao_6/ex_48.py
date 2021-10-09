"""
48- Faça um programa que some os termos de valor par da sequência
de Fibonacci, cujos valores não ultrapassem quatro milhões.
"""

num, seq_fibonacci, i, soma = 4_000_000, [0, 1], 1, 0

while num <= 0:
    num = int(input('Digite um número: '))

while True:
    if seq_fibonacci[i] < num:
        seq_fibonacci.append(seq_fibonacci[i] + seq_fibonacci[i-1])
    else:
        break
    i += 1

for j in seq_fibonacci:
    if j % 2 == 0:
        soma += j

print(soma)

