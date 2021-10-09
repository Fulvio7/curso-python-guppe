"""
60- Leia vários números até o usuário digitar 0 e imprima:
a - A soma dos números digitados
b - A quantidade de números digitados
c - A média dos números digitados
d - O maior número digitado
e - O menor número digitado
f - A média dos números pares
"""

num, soma, total, maior, menor = -1, 0, 0, float(), float()
soma_pares, total_pares = 0, 0
print('Só para quando digita 0.')
while True:
    num = float(input('Insira um valor: '))
    if num == 0:
        print('Resultados dos números digitados:')
        print(f'Soma: {soma}')
        print(f'Total: {total}')
        print(f'Média: {soma/total}')
        print(f'Maior: {maior}')
        print(f'Menor: {menor}')
        print(f'Média dos pares: {soma_pares/total_pares}')
        break
    else:
        if total == 0:
            maior, menor = num, num
        else:
            if maior < num:
                maior = num
            if menor > num:
                menor = num
        soma += num
        total += 1
        if num % 2 == 0:
            soma_pares += num
            total_pares += 1






