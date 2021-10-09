"""
Entendendo o **kwargs

Ele é só mais um parâmetro, mas diferentemente do *args que coloca
os valores extras em tuplas, o **kwargs exige que utilizemos parâmetros
nomeados, e transforma esses parâmetros extras em um dicionário.

# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Nem *args nem **kwargs são obrigatórios
cores_favoritas()
cores_favoritas(fulvio='vermelho')

# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'fulvio' in kwargs and kwargs['fulvio'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico!'
    elif 'fulvio' in kwargs:
        return f"{kwargs['fulvio']} Fulvio!"
    return 'Não tenho certeza quem é você...'


print(cumprimento_especial())
print(cumprimento_especial(fulvio='Python'))
print(cumprimento_especial(fulvio='Oi'))
print(cumprimento_especial(fulvio='especial'))

Nas funções em Python nós podemos ter, NESTA ORDEM:

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs;


# Exemplo da ordem dos parâmetros


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro(a)')
    else:
        print('Casado(a)')
    print(kwargs, end='\n\n')


minha_funcao(8, nome='Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Importância de manter a ordem na declaração da função

# Função com a ordem CORRETA dos parâmetros


def mostra_info(a, b, *args, instrutor='Fulvio', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='Barichello', cargo='instrutor'))


# Função com a ordem INCORRETA dos parâmetros


def mostra_info(a, b, instrutor='Fulvio', *args,  **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='Barichello', cargo='instrutor'))

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Fúlvio', 'sobrenome': 'Barichello'}

# print(mostra_nomes(nomes))  # TypeError
print(mostra_nomes(**nomes))  # TypeError


"""


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


# O desempacotamento com 1 * funciona para:
lista = [1, 2, 3]
soma_multiplos_numeros(*lista)

tupla = 1, 2, 3
soma_multiplos_numeros(*tupla)

conjunto = {1, 2, 3}
soma_multiplos_numeros(*conjunto)

# Em dicionarios as chaves tem de ter os mesmos nomes dos parâmetros
# para que o desempacotamento funcione
dicionario = {'a': 1, 'b': 2, 'c': 3}
soma_multiplos_numeros(*dicionario)

dicionario = {'d': 1, 'e': 2, 'f': 3}
soma_multiplos_numeros(**dicionario)
