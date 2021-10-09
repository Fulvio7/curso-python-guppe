"""
19- Leia um número entre 100 e 999 e imprima na saída cada um dos
algarismos que compõem o número.
"""

numero = -1
while (numero < 100) or (numero > 999):
    numero = int(input('Digite um número inteiro de 100 a 999: '))

numero = str(numero)

for i in range(3):
    print(numero[i])
