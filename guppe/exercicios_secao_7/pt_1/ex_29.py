"""
29- Faça um programa que receba 6 números inteiros e mostre:
- Os números pares digitados e sua soma
- Os números ímpares e a quantidade de ímpares digitados
"""

lista, pares, impares, soma, qtd_impares = [], [], [], 0, 0

for i in range(6):
    lista.append(int(input(f'Digite o {i+1}º número: ')))

    if lista[i] % 2 == 0:
        pares.append(lista[i])
        soma += lista[i]
    else:
        impares.append(lista[i])
        qtd_impares += 1

print('\nResultados: ')
print(f'Números pares digitados: {pares}')
print(f'Soma dos pares: {soma}')
print(f'Números ímpares digitados: {impares}')
print(f'Quantidade de ímpares: {qtd_impares}')


