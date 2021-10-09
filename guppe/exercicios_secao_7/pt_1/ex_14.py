"""
14- Leia um vetor de 10 posições e verifique se existem valores
iguais, e os escreva na tela.
"""

numeros, numeros_repetidos = [], []
for i in range(10):
    num = int(input('Digite um número: '))

    if num not in numeros:
        numeros.append(num)
    else:
        numeros_repetidos.append(num)

print(end='\n')
print(f'Números distintos: \n{numeros}')
print(f'Números repetidos: \n{set(numeros_repetidos)}')

