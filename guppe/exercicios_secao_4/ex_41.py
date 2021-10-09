"""
41- Leia o valor da hora trabalhada e o número total de horas
trabalhadas. Calcule e imprima o valor a ser pago acrescentando-se
10%.
"""

valor_da_hora = float(input('Digite o valor em reais da hora trabalhada: R$ '))
total_de_horas = float(input('Digite o total de horas trabalhadas: '))

valor_a_ser_pago = valor_da_hora * total_de_horas * 1.1

print(f'O valor a ser pago com acréscimo de 10% é R$ {valor_a_ser_pago:.2f} ')

