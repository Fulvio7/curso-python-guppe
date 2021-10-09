"""
52- Escreva um programa que receba como entrada o valor do saque
realizado pelo cliente de um banco e retorne quantas notas de cada
valor serão necessárias para atender ao saque com a menor quantidade
de notas possíveis. Serão utilizadas notas de 100, 50, 20, 10, 5,
2 e 1 real.
"""
tot_100, tot_50, tot_20, tot_10, tot_5, tot_2, tot_1 = 0, 0, 0, 0, 0, 0, 0
saque = float(input('Digite o valor do saque: R$ '))

while saque > 0:
    if saque - 100 >= 0:
        saque -= 100
        tot_100 += 1
    elif saque - 50 >= 0:
        saque -= 50
        tot_50 += 1
    elif saque - 20 >= 0:
        saque -= 20
        tot_20 += 1
    elif saque - 10 >= 0:
        saque -= 10
        tot_10 += 1
    elif saque - 5 >= 0:
        saque -= 5
        tot_5 += 1
    elif saque - 2 >= 0:
        saque -= 2
        tot_2 += 2
    elif saque - 1 >= 0:
        saque -= 1
        tot_1 += 1
    else:
        break

print('Total de notas: ')
print(f'100 {tot_100}')
print(f' 50 {tot_50}')
print(f' 20 {tot_20}')
print(f' 10 {tot_10}')
print(f'  5 {tot_5}')
print(f'  2 {tot_2}')
print(f'  1 {tot_1}')










