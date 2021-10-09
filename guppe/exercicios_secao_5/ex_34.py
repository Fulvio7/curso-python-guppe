"""
34- Leia a nota e o número de faltas de um aluno. Encontre o conceito
do aluno baseado na tabela abaixo. Veja que ocorre uma redução de
conceito quando o aluno ultrapassa as 20 faltas.
NOTA           CONCEITO <= 20 FALTAS    CONCEITO > 20 FALTAS
>= 9.0  <= 10  A                        B
>= 7.5 < 9.0   B                        C
>= 5.0 < 7.5   C                        D
>= 4.0 < 5.0   D                        E
>= 0.0 < 4.0   E                        E
"""

conceito = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}

nota = float(input('Digite a nota do aluno: '))
faltas = float(input('Digite o número de faltas: '))

conceito_id = int

if 9 <= nota <= 10:
    conceito_id = 1

elif 7.5 <= nota < 9:
    conceito_id = 2

elif 5 <= nota < 7.5:
    conceito_id = 3

elif 4 <= nota < 5:
    conceito_id = 4

elif 0 <= nota < 4:
    conceito_id = 5

if faltas > 20 and conceito_id < 5:
    conceito_id += 1

print(f'O cenceito do aluno foi: {conceito[conceito_id]}.')


