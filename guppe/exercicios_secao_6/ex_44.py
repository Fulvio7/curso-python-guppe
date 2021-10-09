"""
44- Leia um número positivo do usuário. Calcule e imprima a sequência
Fibonacci até o primeiro número superior ao número lido.
Exemplo: 30  ->  0 1 1 2 3 5 8 13 21 34.
"""
num, seq_fibonacci, i = 0, [0, 1], 1

while num <= 0:
    num = int(input('Digite um número: '))

while True:
    if seq_fibonacci[i] <= num:
        seq_fibonacci.append(seq_fibonacci[i] + seq_fibonacci[i-1])
    else:
        break
    i += 1

print(seq_fibonacci)

