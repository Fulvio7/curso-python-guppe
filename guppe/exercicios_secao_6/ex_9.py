"""
9- Leia um número inteiro N e depois imprima os N primeiros
números naturais ímpares.
"""

n = int(input('Digite o valor de N: '))
cont = 0
numero = 0
while True:
    if cont == n:
        break
    else:
        numero += 1
    if numero % 2 == 1:
        print(numero)
        cont += 1

