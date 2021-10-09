"""
12- Leia 5 valores. Mostre todos os números digitados, além do maior,
do menor e da média dos 5.
"""

numeros, maior, menor, soma = [], float(), float(), float()

for i in range(5):
    numeros.append(float(input(f'Digite o {i+1}º número: ')))

    soma += numeros[i]

    if i == 0:
        maior, menor = numeros[i], numeros[i]
    else:
        if maior < numeros[i]:
            maior = numeros[i]
        if menor > numeros[i]:
            menor = numeros[i]

print(f'Números inseridos: {numeros}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Média: {soma/5}')


