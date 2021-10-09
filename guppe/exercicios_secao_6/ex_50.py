"""
50- Chico tem 1,5 m e cresce 2 cm por ano, enquanto Zé tem 1,1 m e
cresce 3 cm por ano. Escreva um programa que calcule e imprima
quantos anos serão necessários para que Zé seja maior que Chico.
"""

alt_chico, alt_ze, anos = 1.5, 1.1, 0

while True:
    alt_chico += 0.2
    alt_ze += 0.3
    if alt_ze >= alt_chico:
        print(f'Zé fica maior que Chico após {anos} anos.')
        break
    anos += 1
