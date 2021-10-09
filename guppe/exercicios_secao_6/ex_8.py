"""
8- Leia 10 números e ao final imprima o maior e o menor.
"""
maior = float()
menor = float()
for i in range(1, 11):
    num = float(input(f'Digite o n{i}: '))
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'Maior: {maior}')
print(f'Menor: {menor}')



