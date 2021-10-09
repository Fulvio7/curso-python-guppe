"""
9- Leia o salário de um trabalhador e o valor de uma parcela de um
empréstimo. Se a prestação for maior que 20% do salário imprima
'Empréstimo não concedido', caso contrário imprima 'Empréstimo
concedido'.
"""

salario = float(input('Digite o seu salário: R$ '))
parcela = float(input('Digite o valor da parcela: R$ '))

percentual = parcela / salario

if percentual > 0.2:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')


