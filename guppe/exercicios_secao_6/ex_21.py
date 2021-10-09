"""
21- Leia dois número. Calcule e mostre:
- a soma dos números pares desse intervalo de números, incluindo os
números digitados.
- a multiplicação dos números ímpares deste intervalo, incluindo os
números digitados.
"""
print('Digite um intervalo')
n1 = int(input('Digite o número menor n1: '))
n2 = int(input('Digite o número maior n2: '))

soma_pares, produto_impares = 0, 1

for i in range(n1, n2+1):
    if i % 2 == 0:
        soma_pares += i
    else:
        produto_impares *= i

print(f'Soma dos pares: {soma_pares}')
print(f'Produto dos ímpares: {produto_impares}')
