"""
61- Faça um programa que calcule o maior número palíndromo feito
a partir do produto de dois números de 3 dígitos. Exemplo:
O maior palíndromo feito a partir do produto de dois números de dois
dígitos é 9009 = 91*99
"""
maior = int()
for i in range(100, 1000):
    for j in range(100, 1000):
        frente = str(i*j)
        tras = (str(i*j)[::-1])
        if frente == tras:
            if maior < i * j:
                maior = i * j

print(maior)

