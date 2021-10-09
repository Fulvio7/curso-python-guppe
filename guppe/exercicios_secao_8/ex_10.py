"""
10- Faça uma função que receba dois números e retorne qual deles
é o maior.
"""


def retorna_maior(n1, n2):
    if n1 > n2:
        return f'{n1} é maior.'
    elif n2 > n1:
        return f'{n2} é maior.'
    return 'Os dois números são iguais! XP '


print('Descubra o maior número')
num1 = int(input('Num1 = '))
num2 = int(input('Num2 = '))

print(retorna_maior(num1, num2))




