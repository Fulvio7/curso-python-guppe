"""
42- Faça um programa que leia um conjunto não determinado de valores,
um de cada vez, e escreva para cada um dos valores lidos:
o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com
um valor negativo ou zero.
"""
print('O quadrado, o cubo e a raiz quadrada')
while True:
    num = float(input('\nNúmero: '))
    if num <= 0:
        break
    print(f'{num} ao quadrado = {num**2}')
    print(f'{num} ao cubo = {num**3}')
    print(f'raiz quadrada de {num} = {num**(1/5)}')

