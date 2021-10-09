"""
15- Leia um vetor com 20 números inteiros. Escreva os elementos do
vetor eliminando os repetidos.
"""

numeros = []
print('Digite 20 números inteiros: ')
for _ in range(20):
    numeros.append(int(input('Número: ')))

print(f'Números distintos que foram digitados: \n{set(numeros)}')





