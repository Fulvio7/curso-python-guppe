"""
20- Leia três lados e verifique se eles formam um triângulo (um dos
lados não pode ser maior que a soma dos outros dois e este lado deve
ser menor que o valor absoluto da diferença entre eles). Caso formem
um triângulo, mostre qual tipo:
-> equilátero: três lados iguais;
-> isósceles: dois lados iguais;
-> escaleno: três lados diferentes.
"""
print('=== VERIFICANDO TRIANGULIDADES ===')
lado_a = float(input('Digite o tamanho do lado A: '))
lado_b = float(input('Digite o tamanho do lado B: '))
lado_c = float(input('Digite o tamanho do lado C: '))

if (lado_a + lado_b > lado_c > abs(lado_a - lado_b)) \
        and (lado_b + lado_c > lado_a > abs(lado_b - lado_c)) \
        and (lado_a + lado_c > lado_b > abs(lado_a - lado_c)):
    if lado_a == lado_b == lado_c:
        print('Triângulo equilátero.')
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        print('Triângulo isósceles.')
    elif lado_a != lado_b != lado_c:
        print('Triângulo escaleno.')
else:
    print(f'Os lados {lado_a}, {lado_b} e {lado_c} não formam um triângulo.')

