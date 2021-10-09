"""
17- Leia uma matriz 10x3 com as notas de 10 alunos em 3 provas.
Em seguida, escreva o número de alunos cuja pior nota foi na prova 1,
quantos a pior nota foi na prova 2 e quantos na prova 3. Em cado de
empate das notas de um aluno, o critério de desempate é arbitrário, mas
o aluno deve ser contabilizado apenas uma vez.
"""
notas_alunos = [[], [], [], [], [], [], [], [], [], []]
piores_provas = [0, 0, 0]
menor, posicao = float(), int()

print('Notas dos Alunos')
for i in range(10):
    print(f'\nAluno {i}: ')
    for j in range(3):
        notas_alunos[i].append(float(input(f'{j+1}ª prova = ')))

        if j == 0:
            menor = notas_alunos[i][j]
            posicao = j
        else:
            if menor > notas_alunos[i][j]:
                menor = notas_alunos[i][j]
                posicao = j

    if posicao == 0:
        piores_provas[0] += 1
    elif posicao == 1:
        piores_provas[1] += 1
    elif posicao == 2:
        piores_provas[2] += 1

print('\nQuantidade de alunos com as piores notas, por prova: ')
for i in range(3):
    print(f'Prova {i+1}: {piores_provas[i]} alunos.')














