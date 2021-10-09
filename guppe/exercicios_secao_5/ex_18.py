"""
18- Mostre 4 opções de operações matemáticas para o usuário.
O usuário escolhe uma das opções, e logo após deve digitar 2 números.
O seu programa deve realizar a operação e mostrar o resultado.
"""

operadores = ['+', '-', '*', '/']

operacao = input('Selecione uma das operações:'
                 '\n[+] => SOMA'
                 '\n[-] => SUBTRAÇÃO'
                 '\n[*] => MULTIPLICAÇÃO'
                 '\n[/] => DIVISÃO\n')

if operacao in operadores:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if operacao == '+':
        print(f'{n1} + {n2} = {n1 + n2}')
    elif operacao == '-':
        print(f'{n1} - {n2} = {n1 - n2}')
    elif operacao == '*':
        print(f'{n1} x {n2} = {n1 * n2}')
    elif operacao == '/':
        print(f'{n1} / {n2} = {n1 / n2}')
else:
    print(f'Erro: Operação selecionada diferente de {operadores}')


