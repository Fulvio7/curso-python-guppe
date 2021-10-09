"""
42- Receba o salário-base de um funcionário, calcule e imprima o
resultado, sabendo-se que o funcionário:
- tem uma gratificação de 5% do salário-base;
- paga 7% de imposto sobre o salário-base.
"""

salario_base = float(input('Digite o valor do salário-base R$ '))

gratificacao = 0.05 * salario_base
impostos = 0.07 * salario_base

salario_a_receber = salario_base + gratificacao - impostos

print(f'O funcionário deve receber R$ {salario_a_receber:.2f} ')
