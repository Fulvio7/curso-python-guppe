"""
16- Usando switch, leia um número inteiro entre 1 e 12 e mostre o
mês correspondente. Exemplo: 1 janeiro, 2 fevereiro...
"""

mes = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março',
       4: 'Abril', 5: 'Maio', 6: 'Junho',
       7: 'Julho', 8: 'Agosto', 9: 'Setembro',
       10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

num = int(input('Digite um número inteiro de 1 à 12: '))

print(f'Você selecionou o mês de {mes[num]}.')




