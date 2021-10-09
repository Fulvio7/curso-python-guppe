"""
5- Leia 10 valores digitados pelo usuário e some-os.
"""

num = float()
soma = float()

print('=== SOMADOR ===')
for i in range(1, 11):
    num = float(input(f'Digite n{i}: '))
    soma += num

print(soma)

