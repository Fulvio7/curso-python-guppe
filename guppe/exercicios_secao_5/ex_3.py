"""
3- Leia um número real. Se ele for positivo imprima a sua raiz quadrada,
se ele for negativo imprima o número ao quadrado.
"""
from math import sqrt
numero = float(input('Digite um número: '))

if numero > 0:
    print(f'A raiz quadrada de {numero} é {sqrt(numero):.4f}. ')
elif numero < 0:
    print(f'Elevando-se {numero} ao quadrado temos {numero ** 2}. ')
else:
    print(f'Você digitou {numero:.0f}. ')
