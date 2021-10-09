"""
47- Leia um número de 4 dígitos e imprima cada algarismo em uma linha.
"""

numero = input('Digite um numero de 4 dígitos: ')

if numero.isnumeric():
    if len(numero) == 4:
        print(f'{numero[0]} é o milhar ')
        print(f'{numero[1]} é a centena ')
        print(f'{numero[2]} é a dezena ')
        print(f'{numero[3]} é a unidade ')
    elif len(numero) < 4:
        print('Erro: número com menos de 4 dígitos. ')
    else:
        print('Erro: número com mais de 4 dígitos. ')
else:
    print(f'Erro: {numero} não é um número. ')
"""

    """

