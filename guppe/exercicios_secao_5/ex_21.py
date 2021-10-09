"""
21- Leia a opção selecionada pelo usuário e execute a operação
escolhida, de acordo com o menu abaixo. Em caso de erro apresente a
uma mensagem de erro.
"""

print('Escolha a opção:'
      '\n1- Soma de 2 números.'
      '\n2- Diferença entre 2 números (maior pelo menor).'
      '\n3- Produto entre 2 números.'
      '\n4- Divisão entre 2 números (o denominador não pode ser zero).')
opcao = input('Opção ')

if opcao not in ['1', '2', '3', '4']:
    print('Erro: Opção inválida.')
else:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if opcao == '1':
        print(f'{n1} + {n2} = {n1 + n2}')

    elif opcao == '2':
        if n1 > n2:
            print(f'{n1} - {n2} = {n1 - n2}')
        else:
            print(f'{n2} - {n1} = {n2 - n1}')

    elif opcao == '3':
        print(f'{n1} x {n2} = {n1 * n2}')

    elif opcao == '4':
        if n2 == 0:
            print('Erro: o denominador não pode ser zero.')
        else:
            print(f'{n1} / {n2} = {n1 / n2}')
