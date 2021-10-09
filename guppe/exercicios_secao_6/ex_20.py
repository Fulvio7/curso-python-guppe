"""
20- Leia uma sequência de números inteiros. O processo termina
quando for informado o valor 1000. Imprima quantos números foram
lidos e quantos são pares.
"""
total_pares, total_numeros = 0, 0
while True:
    numero = int(input('Digite um número inteiro: '))
    total_numeros += 1
    if numero % 2 == 0:
        total_pares += 1
    if numero == 1000:
        break

print(f'Foram inseridos {total_numeros} números.')
print(f'Destes, {total_pares} são pares.')
