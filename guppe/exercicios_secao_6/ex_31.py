"""
31- Calcule e escreva o valor de S:
S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""
soma = 0
for i in range(1, 51):
    soma += ((2*i) - 1) / i

print(soma)

