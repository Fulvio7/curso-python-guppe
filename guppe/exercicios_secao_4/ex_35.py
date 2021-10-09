"""
35- Faça um programa que receba os catetos A e B, calcule a hipotenusa
e a imprima. A equação da hipotenusa é:
hip = sqrt((a ** 2) + (b ** 2))
"""
import math

cat_a = float(input('Digite o cateto A '))
cat_b = float(input('Digite o cateto B '))

hip = math.sqrt((cat_a ** 2) + (cat_b ** 2))

print(f'A hipotenusa é {hip}')


