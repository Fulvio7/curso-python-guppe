"""
10- Leia a nota de 15 alunos e armazene-as em um vetor. Calcule e
imprima a média geral.
"""

notas, soma = [], float()

for i in range(15):
    notas.append(float(input(f'Digite a nota do aluno {i}: ')))

    soma += notas[i]

print(f'Todas as notas: \n{notas}')
print(f'Nota média da turma: {soma/15}')
