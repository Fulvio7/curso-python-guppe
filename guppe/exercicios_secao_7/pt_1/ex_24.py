"""
24- Leia 10 pares de números, sendo primeiro o código do aluno e o
segundo a sua altura. Ao final imprima o código e altura do aluno
mais alto e o código e a altura do aluno mais baixo.
"""

aluno, altura = float(), float()
maior_altura, menor_altura = float(), float()
alunos_altos, alunos_baixos = [], []

print('Alunos e suas Alturas')
for i in range(10):
    aluno = float(input(f'\nCódigo aluno {i}: '))
    altura = float(input('Altura: '))

    if i == 0:
        maior_altura = altura
        alunos_altos.append(aluno)
        menor_altura = altura
        alunos_baixos.append(aluno)
    else:
        if maior_altura < altura:
            maior_altura = altura
            alunos_altos.clear()
            alunos_altos.append(aluno)
        elif maior_altura == altura:
            alunos_altos.append(aluno)

        if menor_altura > altura:
            menor_altura = altura
            alunos_baixos.clear()
            alunos_baixos.append(aluno)
        elif menor_altura == altura:
            alunos_baixos.append(aluno)

print(f'\nAlunos mais altos: {alunos_altos}, com {maior_altura:.2f}m')
print(f'Alunos mais baixos: {alunos_baixos}, com {menor_altura:.2f}m')


