"""
35- Leia dois números e some os ímpares no intervalo entre estes
dois números. Caso o primeiro número seja menor que o segundo,
imprima a mensagem: "Intervalo de valores inválido" e o programa
termina.
"""
soma = 0
ni = int(input('Digite o valor inicial: '))
nf = int(input('Digite o valor final: '))

if nf >= ni:
    for i in range(ni, nf+1):
        if i % 2 != 0:
            soma += i
    print(f'Soma dos ímpares neste intervalo: {soma}')
else:
    print('Intervalo de valores inválidos')

