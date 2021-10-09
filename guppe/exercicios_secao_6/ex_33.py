"""
33- Dados n e dois números inteiros positivos, i e j, diferentes de 0,
imprimir em ordem crescente os n primeiros números naturais que são
múltiplos de i ou de j. Exemplo:
n=6, i=2, j=3 -> Saída = 0,2,3,4,6,8.
"""
n, i, j, cont, multiplos, total_multiplos = -1, -1, -1, 0, [], 0

while n < 0:
    n = int(input('Digite n: '))
while i < 0:
    i = int(input('Digite i: '))
while j < 0:
    j = int(input('Digite j: '))

while total_multiplos < n:
    if (cont % i == 0) or (cont % j == 0):
        multiplos.append(cont)
        total_multiplos += 1
    cont += 1

print(f'{n} múltiplos de {i} e {j}:\n{multiplos}')

