"""
Tuplas (tuple)

São muito parecidas com as listas.
Existindo basiccamente duas diferenças:
1- São representadas por () parênteses.
2- São imutáveis, uma vez criadas não podem ser modificadas.

# Cuidado 1
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6  # sem parênteses também funciona!
print(tupla2)
print(type(tupla2))


# Cuidado 2: tuplas com um elemento
tupla3 = (4)  # isso NÃO é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # isso é uma tupla!
print(type(tupla4))
print(tupla4)

# Tuplas são definidas pelas vírgulas e não pelos parênteses
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tuplas é igual a de listas
tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# Não existem métodos de inserção e exclusão em tuplas,
# justamente pelo fato delas serem imutáveis.

# Podemos utilizar os métodos de soma, máximo, mínimo e tamanho
# desde que sejam todos numéricos
tupla = 1, 2, 3, 4, 5, 6

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenamento de tuplas

tupla1 = 1, 2, 3
print(tupla1)

tupla2 = 4, 5, 6
print(tupla2)

print(tupla1 + tupla2)  # tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

# são imutáveis mas podemos sobrescrever seus valores
tupla1 = tupla1 + tupla2
print(tupla1)

# Verificar se determinado elemento está na tupla

tupla = 1, 2, 3

print(3 in tupla)
print(4 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# contando elementos de uma tupla

tupla = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

# Dicas na utilização de tuplas:
# SEMPRE que não precizarmos alterar uma coleção

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Acesso de elementos
print(meses[1])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificando o índice de um elemento
print(meses.index('Outubro'))

# Slicing
# tupla[inicio:fim:passo]
print(meses[3:10:2])
print(meses[::-1])

# Vantagens de tuplas:
# São mais rápidas que listas
# Deixam seu código mais seguro, devido sua imutabilidade

"""

tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)






