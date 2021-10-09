"""
10- Receba a altura e o sexo de uma pessoa, calcule e mostre seu peso
ideal. Utilize as fórmulas:
Homens: (72.7 * altura) - 58
Mulheres: (62.1 * altura) - 44.7
"""

print('===== DESCUBRA SEU PESO IDEAL =====')
sexo = input('Digite o seu sexo (m ou f): ').lower()
altura = float(input('Digite sua altura em metros: '))

peso_ideal = float

if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {peso_ideal:.3f} kg')
elif sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso_ideal:.3f} kg')
else:
    print('Erro: Sexo inválido.')

