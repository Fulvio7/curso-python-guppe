"""
45- Faça um programa que converta km/h para m/s e vice versa quantas
vezes desejar. Deve ser desenvolvido um menu com as duas opções
mais uma terceira para sair da execução.
"""

while True:
    print('=== CONVERSOR ===')
    print('[ A ] - km/h -> m/s')
    print('[ B ] - m/s -> km/h')
    print('[ Q ] - Sair ')
    opcao = ''
    while opcao != 'A' and opcao != 'B' and opcao != 'Q':
        opcao = input('Insira a opção desejada: ').upper()

    if opcao == 'A':
        velo = float(input('km/h: '))
        print(f'm/s = {velo/3.6}\n')
    elif opcao == 'B':
        velo = float(input('m/s: '))
        print(f'km/h = {velo*3.6}\n')
    else:
        print('Obrigado e até a próxima!')
        break
