"""
17- Faça um programa que calcule e mostre a área de um trapézio.
A sua equação é:
área = (base_maior + base_menor) * altura / 2
"""

base_maior = float(input('Digite o tamanho da base maior: '))
base_menor = float(input('Digite o tamanho da base menor: '))
altura = float(input('Digite a altura: '))

if base_maior > 0 and base_menor > 0 and altura > 0:
    area = (base_maior + base_menor) * altura / 2
    print(f'A área do trapézio é {area}')
else:
    print('Erro: Todos os números devem ser maior do que zero.')


