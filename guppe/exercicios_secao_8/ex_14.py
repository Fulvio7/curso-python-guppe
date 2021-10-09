"""
14- Faça uma função que receba a distância em km e a quantidade de litros
de gasolina consumidos por um carro em um percurso, calcule o consumo em
km/l e escreva uma mensagem de acordo com a tabela abaixo:
CONSUMO (km/l)  MENSAGEM
menor que 8     Venda o carro!
entre 8 e 14    Econômico!
maior que 14    Super econômico!
"""


def consumo(distancia, litros):
    eficiencia = distancia / litros
    if eficiencia < 8:
        return 'Venda o carro!'
    elif eficiencia > 14:
        return 'Super econômico!'
    return 'Econômico!'


print('Calculadora de consumo')
km = float(input('Digite a distância em km: '))
li = float(input('Digite a quantidade em l: '))

print(consumo(km, li))








