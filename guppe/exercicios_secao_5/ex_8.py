"""
8- Leia duas notas de um aluno. Se as duas notas forem válidas (entre
0.0 e 10.0) imprima a média, caso sejam inválidas, informe o usuário
e finalize o programa.
"""

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
    print('Valor de nota inválido (menor que 0 ou maior que 10).')
else:
    media = (n1 + n2) / 2
    print(f'A média das notas é {media}')

