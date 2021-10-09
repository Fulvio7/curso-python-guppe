"""
4- Leia e armazene um vetor de 8 posições, leia também X e Y,
correspondentes a duas posições do vetor. Calcule e imprima a soma dos
valores das posições X e Y.
"""

vet, posX, posY = [], -1, -1

for i in range(8):
    vet.append(float(input(f'Digite vetor[{i}]: ')))

while posX < 0 or posX > 7:
    posX = int(input(f'Digite um valor para X entre 0 e 7: '))

while posY < 0 or posY > 7:
    posY = int(input(f'Digite um valor para Y entre 0 e 7: '))

print(f'A soma entre vetor[{posX}] e vetor[{posY}] é: ')
print(f'{vet[posX]} + {vet[posY]} = {vet[posX] + vet[posY]}')


