"""
41- Faça um programa que calcule a associação de dois resistores em
paralelo, conforme a equação abaixo. O programa deve continuar
executando até que um valor de resistor igual a zero seja digitado.
R = (R1 * R2) / (R1 + R2)
"""
print('Calculando 2 resistores em paralelo:')
print('R = (R1 * R2) / (R1 + R2)')
while True:
    r1 = float(input('R1: '))
    if r1 <= 0:
        break
    r2 = float(input('R2: '))
    if r2 <= 0:
        break
    erre = (r1 * r2) / (r1 + r2)
    print(f'R = {erre}')

