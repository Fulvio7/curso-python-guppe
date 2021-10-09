"""
47- Faça uma calculadora, com o menu:
adição, subtração, multiplicação, divisão, saída.
O usuário poderá realizar quantas operações desejar entre dois números
Até que a opção de saída seja selecionada.
"""

while True:
    print('CALCULADORA + - * /')
    print('[ 1 ] - ADIÇÃO ')
    print('[ 2 ] - SUBTRAÇÃO ')
    print('[ 3 ] - MULTIPLICAÇÃO ')
    print('[ 4 ] - DIVISÃO ')
    print('[ 5 ] - SAIR ')
    opcao = 0
    while opcao < 1 or opcao > 5:
        opcao = int(input('Opção: '))

    if opcao == 1:
        print('SOMA')
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))
        print(f'{n1} + {n2} = {n1+n2}\n')
    elif opcao == 2:
        print('SUBTRAÇÃO')
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))
        print(f'{n1} - {n2} = {n1-n2}\n')
    elif opcao == 3:
        print('MULTIPLICAÇÃO')
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))
        print(f'{n1} x {n2} = {n1*n2}\n')
    elif opcao == 4:
        print('DIVISÃO')
        n1 = float(input('n1: '))
        n2 = 0
        while n2 == 0:
            n2 = float(input('n2 (diferente de 0): '))
        print(f'{n1} + {n2} = {n1/n2}\n')
    else:
        print('Obrigado por usar a calculadora!')
        break
