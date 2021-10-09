"""
13- Leia 3 notas de um aluno. A primeira e a segunda tem peso 1 e a
terceira tem peso 2. Mostrar a média e se o aluno foi aprovado com
média superior a 60 pontos.
"""

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

media_poderada = (n1 + n2 + (n3 * 2)) / 4

if media_poderada > 60:
    print(f'Aluno aprovado. Média: {media_poderada}')
else:
    print(f'Aluno reprovado. Média: {media_poderada}')
