"""
2- Faça uma função que receba a data atual (dia, mês e ano inteiro) e
exiba-a na tela no formato textual por extenso. Exemplo:
Data: 01/01/2000 -> Imprimir 1 de janeiro de 2000.
"""


def data_por_extenso(dia, mes, ano):
    return f'Data por extenso: \n{dia} de {meses[mes_digitado]} de {ano}'


dia_digitado = 0
mes_digitado = 0
ano_digitado = 0
meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril',
         5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
         9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}

while dia_digitado < 1 or dia_digitado > 31:
    dia_digitado = int(input('Digite o dia: '))

while mes_digitado < 1 or mes_digitado > 12:
    mes_digitado = int(input('Digite o mês: '))

while ano_digitado < 1 or ano_digitado > 2100:
    ano_digitado = int(input('Digite o ano: '))

print(data_por_extenso(dia_digitado, mes_digitado, ano_digitado))


