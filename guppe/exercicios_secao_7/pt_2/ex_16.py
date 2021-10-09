"""
16- Faça um programa para corrigir uma prova com 10 questões de múltipla
escolha (a, b, c, d ou e), em uma turma com 3 alunos. Cada questão vale
1 ponto. Leia o gabarito, e para cada aluno leia sua matrícula (número
inteiro) e suas respostas. Calcule e escreva para cada aluno: sua
matrícula, seus respostas, e sua nota. O percentual de aprovação é
média 7.0.
"""

opcoes = ('a', 'b', 'c', 'd', 'e')
respostas = [[], [], []]
gabarito, matriculas, pontuacao = [], [], []

print('Preencha o gabarito:')
for i in range(10):
    aux = ''
    while aux not in opcoes:
        aux = input(f'{i} - ')
    gabarito.append(aux)

print('Preencha as respostas')
for i in range(3):
    pontos = 0
    matriculas.append(int(input(f'Matrícula do Aluno {i}: ')))
    print(f'Respostas do Aluno {matriculas[i]}: ')
    for j in range(10):
        aux = ''
        while aux not in opcoes:
            aux = input(f'{j} - ')
        respostas[i].append(aux)

        if respostas[i][j] == gabarito[j]:
            pontos += 1

    pontuacao.append(pontos)

print('Pontuação final:')
for i in range(3):
    print(f'Aluno {matriculas[i]}: {pontuacao[i]} pontos.')

