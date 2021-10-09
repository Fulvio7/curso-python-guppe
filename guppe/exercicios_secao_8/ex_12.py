"""
12- Escreva uma função que receba um número inteiro maior do que zero
e retorne a soma de todos os seus algarismos. Exemplo:
entrada: 251 -> processamento: 2 + 5 + 1 -> saída: 8
Obs: Caso o número de entrada não for maior que zero, o programa
terminará com a mensagem 'Número inválido'
"""


def soma_algarismos(numero):
    if int(numero) > 0:
        soma = 0
        for algarismo in numero:
            soma += int(algarismo)
        return f'A soma dos algarismos de {numero} é {soma}.'
    return 'Número inválido'


inteiro = input('Digite um número inteiro: ')

print(soma_algarismos(inteiro))







