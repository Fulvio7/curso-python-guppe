"""
28- Leia 3 números inteiros positivos e calcule a média selecionada
através de um valor numérico digitado pelo usuário. Tipo de médias:
Geométrica  raiz_cubica(x * y * z)
Ponderada   (x + 2*y + 3*z) / 6
Harmônica   1 / ((1/x) + (1/y) + (1/z))
Aritmética  (x + y + z) / 3
"""

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
z = int(input('Digite o valor de z: '))

if x < 0 or y < 0 or z < 0:
    print('Erro: Todos os números devem ser positivos.')
else:
    print('Selecione o tipo de média que deseja:'
          '\n[1] Geométrica'
          '\n[2] Ponderada'
          '\n[3] Harmônica'
          '\n[4] Aritmética')
    opcao = int(input('Opção: '))

    if opcao == 1:
        media = (x * y * z) ** (1/3)
        print(f'Média geométrica {media}')

    elif opcao == 2:
        media = (x + 2*y + 3*z) / 6
        print(f'Média ponderada {media}')

    elif opcao == 3:
        media = 1 / ((1/x) + (1/y) + (1/z))
        print(f'Média harmônica {media}')

    elif opcao == 4:
        media = (x + y + z) / 3
        print(f'Média aritmética {media}')

    else:
        print('Erro: Opção inválida.')
