"""
23- Leia um número inteiro positivo e mostre seus divisores.
"""
number = -1
while number <= 0:
    number = int(input('Type a positive number: '))

for i in range(1, number+1):
    if number % i == 0:
        print(i)


