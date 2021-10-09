"""
25- Calcule as raízes de uma equação de 2° grau. Lembrando que:
x = (-b +- sqrt(delta)) / 2a
delta = b ** 2 - 4ac

Se a for igual a zero não é equação do segundo grau. Mostre a mensagem:
'Não é equação de segundo grau'
Se delta for negativo, não existe raiz real. Mostre 'Não existe raiz'.
Se delta for igual a zero, existe uma raiz. Mostre a raiz e 'Raiz única'.
Se delta for maior que zero, imprima as duas raízes.
"""
from math import sqrt

print('=== CALCULADORA DE EQUAÇÃO DE SEGUNDO GRAU ===')

a = float(input('Digite o valor de a: '))

if a > 0:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print('Não existe raiz')

    elif delta == 0:
        raiz = (- b) / (2 * a)
        print(f'Raiz única: {raiz} ')

    else:
        raiz_1 = (- b + sqrt(delta)) / (2 * a)
        raiz_2 = (- b - sqrt(delta)) / (2 * a)
        print(f'Raízes: {raiz_1} e {raiz_2}')

else:
    print('Não é equação de segundo grau')






