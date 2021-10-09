"""
44- Leia a altura de um degrau e a altura total que o usuário deseja
subir, calcule e imprima o total de degraus que a escada deve ter.
"""
import math

altura_degrau = float(input('Digite a altura do degrau em metros '))
altura_total = float(input('Digite a altura total que deseja subir '))

if altura_degrau != 0:
    num_degraus = altura_total / altura_degrau
    print(f'A escada deve ter {math.ceil(num_degraus)} degraus. ')
else:
    print('Erro: Digite uma altura do degrau maior ou igual a zero.')


