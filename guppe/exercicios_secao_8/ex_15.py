"""
15- Crie um programa que receba três lados (obrigatoriamente maiores que
zero). elabore funções para
a- determinar se estes lados formam um triângulo. Para isso o comprimento
de cada lado é menor que a soma dos outros dois.
b- determinar e mostrar o tipo de triângulo formado, caso ele exista.
Obs: Tipos de triângulos:
Equilátero: três lados iguais
Isósceles: dois lados iguais
Escaleno: três lados diferentes
"""


def forma_trinangulo(lado_1, lado_2, lado_3):
    if (lado_1 < lado_2 + lado_3) \
            and (lado_2 < lado_1 + lado_3) \
            and (lado_3 < lado_1 + lado_2):
        return True
    return False


def testa_triangulo(lado_1, lado_2, lado_3):
    if forma_trinangulo(lado_1, lado_2, lado_3):
        if lado_1 == lado_2 and lado_1 == lado_3:
            return 'Triâgulo Equilátero'
        elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
            return 'Triângulo Isósceles'
        elif lado_1 != lado_2 and lado_1 != lado_3:
            return 'Trângulo Escaleno'
    return 'Os lados informados não formam um triângulo'


l1, l2, l3 = 0, 0, 0

print('Testando um triângulo ')
print('Digite os seus lados ')
while l1 <= 0:
    l1 = float(input('Lado 1: '))
while l2 <= 0:
    l2 = float(input('Lado 2: '))
while l3 <= 0:
    l3 = float(input('Lado 3: '))

print(testa_triangulo(l1, l2, l3))




