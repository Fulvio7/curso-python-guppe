"""
16- Leia um vetor de 5 posições de números reais. Leia também um código
numérico do tipo inteiro. Caso o código não esteja na lista abaixo,
repita a inserção do código.
0 -> finaliza o programa
1 -> imprime o vetor
2 -> imprime o vetor na forma inversa
"""

numeros, codigo = [], -1

for i in range(5):
    numeros.append(float(input(f'Digite o {i+1}º número: ')))

print('\nO que deseja fazer?'
      '\n0 -> Finalizar o programa'
      '\n1 -> Imprimir o vetor'
      '\n2 -> Imprimir o vetor na forma inversa')

while codigo not in (0, 1, 2):
    codigo = int(input('Digite 0, 1 ou 2: '))

if codigo == 0:
    print('Fim do programa.')
elif codigo == 1:
    print(f'\nVetor: \n{numeros}')
elif codigo == 2:
    print(f'\nVetor invertido: \n{numeros[::-1]}')
