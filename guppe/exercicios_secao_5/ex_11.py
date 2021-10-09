"""
11- Leia um número inteiro maior que zero, e devolva a soma de seus
algarismos. Exemplo 251 --> 8 (2 + 5 + 1).
Caso o número não seja maior do que zero deve retornar a mensagem:
'Número inválido'.
# como ainda não foi visto estruturas de repetição,
limitei o tamanho da entrada a 3 dígitos
"""

num = input('Digite um número inteiro de 3 dígitos maior que zero: ')

n0 = int(num[0])
n1 = int(num[1])
n2 = int(num[2])

resultado = n0 + n1 + n2

if resultado > 0:
    print(f'{resultado}')
else:
    print('Número inválido')
