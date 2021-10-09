"""
14- Receba as notas de um aluno (de 0 à 10) referentes a um
trabalho de laboratório (peso 2), uma avaliação semestral (peso 3)
e um exame final (peso 5). Mostre se o aluno está reprovado (de 0 à 2,9),
de recuperação (entre 3 e 4,9) ou se foi aprovado.
"""

nota_trabalho_lab = float(input('Digite a nota do trabalho de laboratório '))
nota_ava_semestre = float(input('Digite a nota da avaliação semestral '))
nota_exame_final = float(input('Digitet a nota do exame final '))

media = ((nota_trabalho_lab * 2) + (nota_ava_semestre * 3)
         + (nota_exame_final * 5)) / 10

if media < 3:
    print(f'Aluno reprovado. Média {media}')
elif media < 5:
    print(f'Aluno em recuperação. Média {media}')
else:
    print(f'Aluno aprovado. Média {media}')




