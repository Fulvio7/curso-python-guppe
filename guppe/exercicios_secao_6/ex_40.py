"""
40- Leia vários números inteiros e só pare quando for digitado
um número negativo. Imprima o maior número e o menor número digitados.
"""

controle, maior, menor = 0, int(), int()

while True:
    digitado = int(input('Digite um número: '))
    if digitado < 0:
        break
    if controle == 0:
        maior, menor = digitado, digitado
        controle = 1
    else:
        if digitado > maior:
            maior = digitado
        if digitado < menor:
            menor = digitado

print(f'Maior = {maior} \nMenor = {menor} ')