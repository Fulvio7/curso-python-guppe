"""
39- Leia a base e a altura e calcule a área deste triângulo.
O programa não pode aceitar medidas menores ou iguais a 0.
"""

base, altura = -1, -1
print('=== ÁREA DO TRIÂNGULO ===')
while base <= 0:
    base = float(input('Digite o tamanho da base: '))

while altura <= 0:
    altura = float(input('Digite o tamanho da altura: '))

area_triangulo = (base**2 + altura**2) / 2

print(f'A = {area_triangulo}')