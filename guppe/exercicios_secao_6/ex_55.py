"""
55- Escreva um programa que leia um número inteiro não negativo n
e imprima a soma dos n primeiros números primos.
"""
n, tot_primos, soma_primos, j = 0, 0, 0, 1
while n <= 0:
    n = int(input('Digite o valor de n: '))

while True:
    divide = 0
    for i in range(1, j+1):
        if j % i == 0:
            divide += 1

    if divide == 2:
        soma_primos += j
        tot_primos += 1

    j += 1
    if tot_primos == n:
        print(f'Soma dos {n} primeiros números primos = {soma_primos}')
        break

