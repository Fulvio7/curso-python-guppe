"""
21- Escreva uma função para determinar a quantidade de números primos
abaixo de N.
"""


def qtde_numeros_primos(parada):
    tot_primos = 0

    for i in range(1, parada+1):
        divide = 0

        for j in range(1, i+1):
            if i % j == 0:
                divide += 1
            if divide > 2:
                break

        if divide == 2:
            tot_primos += 1

    return tot_primos


n = 1
print('Descubra o número de primos até N')

while n <= 1:
    n = int(input('Digite um valor maior que 1 para N: '))

print(qtde_numeros_primos(n))
