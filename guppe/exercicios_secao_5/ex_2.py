"""
2- Leia um número e calcule a sua raiz quadrada. Se o número for
negativo, mostre uma mensagem de número inválido.
"""
from math import sqrt

numero = float(input('Digite um número positivo: '))

if numero < 0:
    print('Erro: Número inválido.')
else:
    print(f'A raiz quadrada de {numero} é {sqrt(numero):.4f}')


