"""
18- Leia a quantidade de números desejada pelo usuário. Imprima o
maior número digitado e quantas vezes ele foi informado.
"""

qtde_numeros = int(input('Informe quantos números deseja digitar: '))
maior, quantas_vezes = int(), 0

for i in range(qtde_numeros):
    num = int(input(f'Digite n{i + 1}: '))
    if i == 0:
        maior = num
        quantas_vezes = 1
    else:
        if num > maior:
            maior = num
            quantas_vezes = 1
        elif num == maior:
            quantas_vezes += 1

print(f'Maior número = {maior}')
print(f'Número de vezes = {quantas_vezes}')



