"""
40- uma empresa contrata um encanador a R$ 30,00 por dia.
Faça um programa que receba o total de dias trabalhados e calcule
o valor total a receber, descontando 8% de imposto de renda.
Imprima o resultado.
"""
valor_por_dia = 30
imposto_de_renda = 0.08

total_de_dias = float(input('Digite o total de dias trabalhados '))

valor_total = total_de_dias * valor_por_dia * (1 - imposto_de_renda)

print(f'O encanador deve receber R$ {valor_total:.2f}')

