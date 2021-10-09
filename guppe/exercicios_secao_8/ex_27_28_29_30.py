"""
Decidi reunir os exercícios 27, 28, 29 e 30 por serem muito similares.
Faça uma função para cada série de Taylor a seguir. Receba como parâmetro
um ângulo em graus. Obs: Variar n de 0 até 5.
27-
sen x = x - x^3/3! + x^5/5! - ... + (-1^n * x^2n-1) / (2n-1)!

28-
cos x = 1 - x^2/2! + x^4/4! - ... + (-1^n * x^2n) / 2n!

29-
senh x = x + x^3/3! + x^5/5! + ... + x^2n-1 / (2n-1)!

30-
cosh x = 1 + x^2/2! + x^4/4! + ... + x^2n / 2n!

"""


def fatorial(numero):
    aux, total = 1, 1
    while aux <= numero:
        total *= aux
        aux += 1
    return total


def seno_taylor(angulo):
    sen = 0
    for n in range(6):
        sen += (((-1)**n) * (angulo**((2*n)-1))) / fatorial((2*n)-1)
    return sen


def cosseno_taylor(angulo):
    return angulo


def seno_hiperb_taylor(angulo):
    return angulo


def cosseno_hiperb_taylor(angulo):
    return angulo


print('Seno, Cosseno, Seno Hiperbólico e Cosseno Hiperbólico')
print('através de série de Taylor')

ang = -1

while ang < 0 or ang > 360:
    ang = float(input('Digite o ângulo em graus [0 ~ 360]: '))

print(f'sen({ang}) = {seno_taylor(ang)}')
print(f'cos({ang}) = {cosseno_taylor(ang)}')
print(f'senh({ang}) = {seno_hiperb_taylor(ang)}')
print(f'cosh({ang}) = {cosseno_hiperb_taylor(ang)}')


