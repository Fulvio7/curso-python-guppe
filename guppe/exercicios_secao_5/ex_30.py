"""
30- Leia 3 números e mostre-os em ordem crescente.
"""
numeros = list()

print('=== ORDENAÇÃO DE 3 NÚMEROS ===')

for i in range(3):
    numeros.append(int(input(f'Digite n{i+1}: ')))

print(f'Números em ordem crescente: \n{sorted(numeros)} ')


