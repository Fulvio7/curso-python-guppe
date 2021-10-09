"""
11- Leia um vetor de 10 números reais. Mostre o total de números ímpares
e a soma dos números positivos.
"""

numeros, total_impares, soma_positivos = [], 0, 0

for i in range(10):
    numeros.append(float(input('Digite um número real: ')))

    if numeros[i] % 2 == 1:
        total_impares += 1

    if numeros[i] > 0:
        soma_positivos += numeros[i]

print(f'Total de números ímpares digitados: {total_impares}')
print(f'Soma dos números positivos: {soma_positivos}')
