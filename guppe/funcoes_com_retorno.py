"""
Funções com retorno
Retornar e imprimir são coisas diferentes!!!
Se utilizarmos o print como saída de uma função, não podemos aproveitar
a sua saída de maneira adequada.
Quando uma função não retorna nada, temos o None.
# Exemplo 1


def quadrado_de_sete():
    print(7**2)


ret = quadrado_de_sete()
print(f'Retorno de quadrado_de_sete: {ret}')

Para que tenhamos um retorno, utilizamos a palavra reservada return.
Não precisamos necessariamente criar uma variável para receber o retorno
de uma função.

# Exemplo 2


def quadrado_de_sete():
    return 7**2


ret = quadrado_de_sete()
print(f'Retorno de quadrado_de_sete: {ret}')

# Exemplo 3


def diz_oi():
    return 'Oi '


alguem = 'Pedro'
print(diz_oi() + alguem + '!')


Observações sobre o return:
1- Ele finaliza uma função
2- Podemos ter em uma função diferentes returns
3- Podemos retornar em uma função qualquer tipo de dado

# Exemplo 1 Ele finaliza uma função


def diz_oi():
    print('Executando antes do retorno')
    return 'Oi '
    print('Executando após o retorno')  # não executa

# Exemplo 2 Podemos ter em uma função diferentes returns


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo 3 Podemos retornar em uma função qualquer tipo de dado


def outra_funcao():
    return 2, 3, 4, 5


n1, n2, n3, n4 = outra_funcao()
print(n1, n2, n3, n4)
print(type(outra_funcao()))


from random import random
# Vamos criar uma função para jogar cara ou coroa


def joga_moeda():  # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
"""

