"""
15- Leia uma matriz 5x10 referente a respostas de 10 questões de
múltipla escolha, referentes a 5 alunos. Leia também um vetor de 10
posições contendo o gabarito de respostas (a, b, c ou d). Seu programa
deverá comparar as respostas de cada candidato com o gabarito e emitir
um vetor denominado resultado, contendo a pontuação correspondente a
cada aluno.
"""
opcoes = ('a', 'b', 'c', 'd')
respostas = [[], [], [], [], []]
corretas, pontuacao = [], [0, 0, 0, 0, 0]

for i in range(5):
    print(f'Digite as respostas do Aluno {i}:')
    for j in range(10):
        res = ''
        while res not in opcoes:
            res = input(f'{j}: ')
        respostas[i].append(res)

print('\nDigite as respostas certas')
for i in range(10):
    res = ''
    while res not in opcoes:
        res = input(f'{i}: ')
    corretas.append(res)

for i in range(5):
    for j in range(10):
        if corretas[j] == respostas[i][j]:
            pontuacao[i] += 1

print('\nPontuação final')
for i in range(5):
    print(f'Aluno {i}: {pontuacao[i]} pontos.')


