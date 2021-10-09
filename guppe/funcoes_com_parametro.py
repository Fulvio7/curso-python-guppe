"""
Funções com parâmetro (de entrada)
São aquelas que recebem dados para serem processadas dentro da mesma.

entrada -> processamento -> saída

# Exemplo 1


def quadrado(numero):
    return numero**2


print(quadrado(7))
print(quadrado(2))

ret = quadrado(3)
print(ret)

# Exemplo 2


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida!')
    print(f'Viva o/a {aniversariante}!')


cantar_parabens('Marcos')

# Exemplo 3


def soma(a, b):  # a e b são parâmetros da função
    return a + b


def multiplica(a, b):
    return a * b


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))  # 2 e 5 são argumentos da função
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Beep '))
print(outra(4, 5, 'Python '))


# Obs: ocorre TypeError se informarmos um número de parâmetros diferente
# do correto

# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    # nome e sobrenome são parâmetros que explicitam o seu valor
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Fúlvio', 'Barichello '))


# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa

# Argumentos Nomeados (Keyword Arguments)

print(nome_completo(nome='Fúlvio', sobrenome='Barichello'))
print(nome_completo(sobrenome='Barichello', nome='Fúlvio'))

# Se nomearmos os argumentos, eles podem ser passados em qualquer ordem


# Devemos sempre tomar cuidado com a posição so return dentro da função

def soma_impares(numeros):
    total = 0
    for i in numeros:
        if i % 2 != 0:
            total += i
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))


tupla = 1, 2, 3, 4, 5, 6, 7
print(soma_impares(tupla))
"""



