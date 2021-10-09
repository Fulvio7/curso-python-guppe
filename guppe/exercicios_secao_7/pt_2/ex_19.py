"""
19- Leia uma matriz 5x4, de 5 alunos, onde:
1ª coluna é o número de matrícula;
2ª coluna é a média das provas;
3ª coluna é a média dos trabalhos;
4ª coluna é a nota final.

a - Leia os primeiros dados dos alunos
b - Calcule a nota final como sendo a soma da média das provas e da
média dos trabalhos
c - Imprima a matrícula do aluno que obteve a maior nota final
d - Imprima a média aritmética das notas finais
"""

notas_alunos = [[int(), float(), float(), float()],
                [int(), float(), float(), float()],
                [int(), float(), float(), float()],
                [int(), float(), float(), float()],
                [int(), float(), float(), float()]]
maior_nota, matriculas_maior_nota = float(), []
soma_notas = 0

print('Preencha os dados dos alunos')
for i in range(5):
    notas_alunos[i][0] = int(input(f'\nMatrícula: '))
    notas_alunos[i][1] = float(input(f'Média das Provas: '))
    notas_alunos[i][2] = float(input(f'Média dos Trabalhos: '))
    notas_alunos[i][3] = notas_alunos[i][1]+notas_alunos[i][2]

    soma_notas += notas_alunos[i][3]

    if i == 0:
        maior_nota = notas_alunos[i][3]
        matriculas_maior_nota.append(notas_alunos[i][0])
    else:
        if maior_nota < notas_alunos[i][3]:
            maior_nota = notas_alunos[i][3]
            matriculas_maior_nota.clear()
            matriculas_maior_nota.append(notas_alunos[i][0])
        elif maior_nota == notas_alunos[i][3]:
            matriculas_maior_nota.append(notas_alunos[i][0])

print('\nResultados: ')
print(f'Média aritmérica das notas finais: {soma_notas/5}')
print(f'Maior nota final: {maior_nota}')
print(f'Matrículas dos alunos com maior nota: {matriculas_maior_nota}')









