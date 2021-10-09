"""
13- Faça uma função que receba dois valores numéricos e um símbolo.
Este símbolo representará a operação que se deseja efetuar com os números,
conforme a tabela abaixo:
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão
"""


def calculadora(n1, n2, operacao):
    if operacao == '+':
        return n1 + n2

    elif operacao == '-':
        return n1 - n2

    elif operacao == '*':
        return n1 * n2

    elif operacao == '/':
        if n2 == 0:
            return f'Erro: divisão por zero.'
        else:
            return n1 / n2


operacoes_validas = ('+', '-', '*', '/')
print('Calculadora com Função')
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

print('Operações válidas: ')
print('[+] -> adição')
print('[-] -> subtração')
print('[*] -> multiplicação')
print('[/] -> divisão')

op = ''
while op not in operacoes_validas:
    op = input('Digite a sua opção: ')

print(calculadora(num1, num2, op))
