"""
9- Leia 6 valores inteiros pares, armazene-os em um vetor e os imprima
em ordem inversa.
"""

vetor_pares = []

for i in range(6):
    num = 1
    while num % 2 != 0:
        num = int(input(f'Digite um número par inteiro: '))
    vetor_pares.append(num)

print(vetor_pares[::-1])

