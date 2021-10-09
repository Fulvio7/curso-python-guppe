"""
1- Faça um programa que determine e mostre os cinco primeiros
múltiplos de 3, considerando números maiores que 0.
"""

numero = 1
cont = 0
while cont < 5:
    if numero % 3 == 0:
        print(numero)
        cont += 1
    numero += 1



