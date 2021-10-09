"""
56- Faça um programa que calcule a soma de todos os números primos
abaixo de dois milhões.
#Funciona, mas depois de 1h e meia não chegou nem na metade...
"""
soma_primos, j = 0, 0
print('Soma dos números primos abaixo de 2.000.000')

while j < 2_000_000:
    divide = 0
    j += 1
    print(j)
    if j % 2 == 1:
        for i in range(1, j+1):
            if j % i == 0:
                divide += 1
            if divide > 2:
                break
    elif j == 2:
        soma_primos += 2

    if divide == 2:
        soma_primos += j


print(soma_primos)

