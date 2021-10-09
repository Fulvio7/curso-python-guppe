"""
28- Leia um número inteiro e positivo, calcule e mostre o valor E,
conforme a fórmula a seguir:
E(n) = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
"""

e_n, fatorial, cont = 1, float(), int

print('Encontrando E(n):')
print('E(n) = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n\n')
n = int(input('Digite o valor de n: '))

for i in range(1, n+1):
    cont = 1
    fatorial = 1
    while cont <= i:
        fatorial *= cont
        cont += 1
    e_n += (1 / fatorial)

print(f'E(n) = {e_n}')
