"""
Entendendo o *args

O *args é um parâmetro como outro qualquer. Começando com '*', é
*args.
O parâmetro *args utilizado em uma função coloca os valores extras
informados como entrada em uma tupla.
Obs: Tuplas são imutáveis.

# Exemplo não muito legal


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))


# Entendendo melhor


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1, 2, 3, 4))

# Podemos misturar parâmetros obrigatórios com *args


def soma_todos_numeros(nome, sobrenome, *args):
    return sum(args)


print(soma_todos_numeros('Fúlvio', 'Barichello'))
print(soma_todos_numeros('Fúlvio', 'Barichello', 1))
print(soma_todos_numeros('Fúlvio', 'Barichello', 1, 2))
print(soma_todos_numeros('Fúlvio', 'Barichello', 1, 2, 3))
print(soma_todos_numeros('Fúlvio', 'Barichello', 1, 2, 3, 4))

# Outro exemplo de *args


def verifica_info(*args):
    if 'Fúlvio' in args and 'Barichello' in args:
        return 'Bem-vindo Fúlvio Barichello'
    return 'Não sei quem você é...'


print(verifica_info())
print(verifica_info('Fúlvio', 'Barichello', 1))
print(verifica_info(1, 'Barichello', 3.145))
print(verifica_info(True, 'Barichello', 'Fúlvio'))
print(verifica_info('Fúlvio', 'Barichello', 1, 2, 3, 4))
"""
# Podemos misturar parâmetros obrigatórios com *args


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]
# print(soma_todos_numeros(numeros))  # TypeError

# Para utilizarmos uma coleção no *args, no caso a lista 'numeros',
# devemos desempacotar o parâmetro antes com '*numeros'

print(soma_todos_numeros(*numeros))




