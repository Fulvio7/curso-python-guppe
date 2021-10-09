"""
54- Leia um número inteiro maior que 1 e verifique se o número é primo
ou não.
"""
divide = 0
print('É primo ou não é?')
num = int(input('Digite um número: '))

for i in range(1, num+1):
    if num % i == 0:
        divide += 1

    if divide > 2:
        break

if divide <= 2:
    print(f'{num} é primo.')
else:
    print(f'{num} não é primo.')
