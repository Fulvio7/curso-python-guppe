"""
37- Faça um programa que verifique quais números entre 1000 e 9999
(inclusive) possuem a propriedade seguinte:
3025  ->  30 + 25 = 55  ->  55**2 = 3025
"""

numeros_legais = list()

for i in range(1_000, 10_000):
    loucura = (int(str(i)[0:2]) + int(str(i)[2:4])) ** 2
    if loucura == i:
        numeros_legais.append(loucura)

print(numeros_legais)
