"""
13- Leia 5 valores e armazene-os em um vetor. Mostre a posição onde se
encontra o maior e o menor valor.
"""

numeros, pos_maior, pos_menor, maior, menor = [], [], [], float(), float()

for i in range(5):
    numeros.append(float(input(f'Digite o número[{i}]: ')))

    if i == 0:
        maior, menor = numeros[i], numeros[i]
        pos_maior.append(i)
        pos_menor.append(i)
    else:
        if maior < numeros[i]:
            maior = numeros[i]
            pos_maior.clear()
            pos_maior.append(i)
        elif maior == numeros[i]:
            pos_maior.append(i)

        if menor > numeros[i]:
            menor = numeros[i]
            pos_menor.clear()
            pos_menor.append(i)
        elif menor == numeros[i]:
            pos_menor.append(i)

print(f'Posições do maior: {pos_maior}')
print(f'Posições do menor: {pos_menor}')




