"""
5- Receba um número inteiro e mostre se ele á par ou ímpar.
"""

number = int(input('Digite um número inteiro: '))

if number == 0:
    print('Você digitou o número zero.'
          '\nEle não é par nem ímpar,'
          '\napesar de possuir propriedades de par.')
elif number % 2 == 0:
    print(f'{number} é par.')
else:
    print(f'{number} é ímpar.')


