"""
30- Leia um valor em reais e a cotação do dólar americano e imprima
o valor correspondente em dólares.
"""

reais = float(input('Digite um valor em reais '))
cotacao = float(input('Digite a cotação do dólar americano '))

dolares = reais / cotacao

print('Convertendo em dólares americanos temos: ')
print(f'R$ {reais:.2f} = US$ {dolares:.2f}')

