"""
26- Leia a distância em km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em
km/l e escreva uma mensagem de acordo com a tabela abaixo:
CONSUMO     km/l    MENSAGEM
menor que   8       Venda o carro!
entre       8 e 14  Econômico!
maior que   12      Super econômico!
"""

distancia = float(input('Digite a distância percorrida em km: '))
qtd_litros = float(input('Digite a quantidade de gasolina em litros: '))

consumo = distancia / qtd_litros

if consumo < 8:
    print('Venda o carro!')
elif 8 <= consumo < 14:
    print('Econômico!')
else:
    print('Super econômico!')
