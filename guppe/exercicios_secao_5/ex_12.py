"""
12- Leia um número inteiro, caso seja positivo calcule seu logaritmo,
caso não seja devolva a mensagem: 'Número inválido'.
"""
import math
num = int(input('Digite um número inteiro positivo: '))

if num > 0:
    loga = math.log10(num)
    print(f'O logarítmo de {num} é {loga}')
else:
    print('Número inválido')



