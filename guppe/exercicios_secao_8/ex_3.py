"""
3- Faça uma função para verificar se um número é positivo ou negativo.
Se o valor for positivo, retorne 1; se for negativo, retorne -1; e se for
0 retorne 0.
"""


def testa_sinal(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    return 0


numero_digitado = int(input('Digite um número inteiro: '))

print(testa_sinal(numero_digitado))



