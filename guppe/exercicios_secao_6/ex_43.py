"""
43- Leia diversas idades e pare quando for digitado um número menor ou
igual a zero. Imprima a média das idades digitadas.
"""
soma, media, cont = 0, 0, 0
print('=== CALCULADORA DE MÉDIA DE IDADES ===')

while True:
    idade = int(input('Idade: '))
    if idade <= 0:
        break
    else:
        soma += idade
        cont += 1

media = soma / cont

print(f'Média: {media:.4f} anos.')


