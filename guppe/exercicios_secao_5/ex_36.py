"""
36- Após ler o valor da venda, calcule e imprima a comissão do
vendedor através da tabela abaixo:
VENDA MENSAL              COMISSÃO
venda >= 100000           700 + 16%
80000 <= venda < 100000   650 + 14%
60000 <= venda < 80000    600 + 14%
40000 <= venda < 60000    550 + 14%
20000 <= venda < 40000    500 + 14%
venda < 20000             400 + 14%
"""

venda = float(input('Digite o valor da vensa mensal: R$ '))

if venda >= 100000:
    comissao = 700 + venda * 1.16
elif 80000 <= venda < 100000:
    comissao = 650 + venda * 1.14
elif 60000 <= venda < 80000:
    comissao = 600 + venda * 1.14
elif 40000 <= venda < 60000:
    comissao = 550 + venda * 1.14
elif 20000 <= venda < 40000:
    comissao = 500 + venda * 1.14
elif venda < 20000:
    comissao = 400 + venda * 1.14

print(f'Comissão R$ {comissao:.2f}')
