"""
15- Usando switch, leia um número inteiro entre 1 e 7 e mostre o dia
da semana correspondente. Exemplo: domingo 1, segunda-feira 2...
"""
# dict
dia_da_semana = {1: 'Domingo',
                 2: 'Segunda-feira',
                 3: 'Terça-feira',
                 4: 'Quarta-feira',
                 5: 'Quinta-feira',
                 6: 'Sexta-feira',
                 7: 'Sábado'}

num = int(input('Digite um número inteiro de 1 à 7: '))

print(f'Você selecionou {dia_da_semana[num]}.')




