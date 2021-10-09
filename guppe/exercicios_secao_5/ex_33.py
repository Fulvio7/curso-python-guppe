"""
33- Leia o preço antigo, calcule o preço novo e escreva a mensagem
de acordo com o prço novo.
PREÇO ANTIGO    % DE AUMENTO
<= 50           5
> 50 e <=100    10
> 100           15

PREÇO NOVO       MENSAGEM
<= 80            Barato
> 80 e <= 120    Normal
> 120 e <= 200   Caro
> 200            Muito caro
"""

print('=== REAJUSTANDO OS PREÇOS ===')
preco = float(input('Digite o preço antigo: R$ '))

# reajustando o preço
if preco <= 50:
    preco *= 1.05
elif preco > 100:
    preco *= 1.15
else:
    preco *= 1.10

# classificando o novo preço
if preco <= 80:
    print('Barato')
elif 80 < preco <= 120:
    print('Normal')
elif 120 < preco <= 200:
    print('Caro')
elif preco > 200:
    print('Muito caro')



