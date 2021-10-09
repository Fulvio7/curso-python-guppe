"""
22- Escreva um programa que permita um aluno inserir suas notas,
válidas entre 10 e 20, e que pare de receber quando a nota for
inválida. Calcule e mostre a média aritmética das notas válidas.
"""

media, nota, total_notas, soma_notas = 0, float(), 0, 0
print('=== CALCULADORA DE MÉDIA ===')
while True:
    nota = float(input('Nota: '))
    if 10 <= nota <= 20:
        soma_notas += nota
        total_notas += 1
    else:
        break

if total_notas > 0:
    media = soma_notas / total_notas

print(f'Média das notas = {media}')



