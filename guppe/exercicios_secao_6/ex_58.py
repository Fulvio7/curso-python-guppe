"""
58- Faça um programa que some os números primos existem entre
a e b, onde a e b são fornecidos pelo usuário.
"""
soma_primos = 0

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

for i in range(a, b+1):
    divide = 0
    for j in range(1, i+1):
        if i % j == 0:
            divide += 1

        if divide > 2:
            break

    if divide == 2:
        soma_primos += i

print(f'Total de números primos no intervalo {a} -- {b}: ')
print(soma_primos)
