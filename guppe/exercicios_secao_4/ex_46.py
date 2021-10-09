"""
46- Leia um numero de 3 dígitos e escreva-o de forma invertida.
Exemplo: 123 fica 321.
"""

numero_lido = input('Digite um número de 3 algarismos ')

numero_gerado = numero_lido[::-1]

print(f'Numero Lido {numero_lido}')
print(f'Numero Gerado {numero_gerado}')
