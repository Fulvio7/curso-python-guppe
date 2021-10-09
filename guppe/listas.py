"""
Listas (list)

Listas em Python são como vetores ou matrizes de outras linguagens,
com a diferença de serem DINÂMICAS e também podermos colocarmos QUALQUER
tipo de dado.

C/Java: Arrays:
- possuem tamanho e tipo de dado fixo;

Python: Listas
-Dinâmica: não possuem tamanho fixo, podemos simplesmente adicionar itens.
-Qualquer tipo de dado: não possuem tipo de dado fixo.

São representadas entre [] - colchetes
São mutáveis, uma vez criadas, podem ser alteradas.

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado número ou string
# está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}.')
else:
    print(f'Não encontrei o número {num}.')

# Podemos facilmente ordenar a nossa lista
lista1.sort()
print(lista1)
lista5.sort()
print(lista5)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))

# Podemos adicionar elementos em uma lista usando .append()
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([0, 3, 8])  # sublista
print(lista1)
if [0, 3, 8] in lista1:
    print(f'Encontrei o número a lista.')

lista1.extend([123, 44, 67])  # coloca cada elemento separado a lista
print(lista1)

# Podemos inserir um novo elemento nna lista informando a
# posição so índice
lista1.insert(2, 'Novo Valor')
print(lista1)

lista6 = lista1 + lista2
print(lista6)

# Podemos inverter uma lista
lista1.reverse()
print(lista1)

# Podemos copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos tem uma lista
print(len(lista5))

# Podemos remover facilmente o último elemento de uma lista
# o pop() ainda retorna este elemento arrancado
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento por índice, e os restantes são
# deslocados para a esquerda (para não ficar buraco)
lista5.pop(5)
print(lista5)
lista5.pop(5)
print(lista5)
lista5.pop(5)
print(lista5)

# Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilemente converter uma string em uma lista

# Exemplo 1
curso = 'Programação Essencial em Python'
print(curso)

# Exemplo 2
curso = 'Programação,Essencial,em,Python'
print(curso.split(','))

lista6 = ['Programação', 'em', 'Python', 'Essencial']
# Convertendo uma lista em string
print(lista6)
curso = ' '.join(lista6)
print(curso)
curso = '$'.join(lista6)
print(curso)

lista6 = [1, 2, 34, True, 'Geek', 'd', [1, 2, 3], 16518465]

# Iterando sobre listas
# Exemplo 1 for

for elemento in lista1:
    print(elemento)

# Exemplo 2 while
carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair"')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Acessamos os itens da lista pelo seu índice
#           0       1           2       3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

# loops
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

print(enumerate(cores))

# Encontrar o índice de um elemento na lista
# se tiver mais de um ele retorna o primeiro encontrado
# se não tiver nenhum ele dá erro
numeros = [5, 6, 7, 5, 8, 9, 10, 9]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice está o valor 9?
print(numeros.index(9))

# Em qual índice está o valor 5, a partir do índice 2?
print(numeros.index(5, 2))

# Buscar o índice de valor 8 entre os índices 3 e 8
print(numeros.index(8, 3, 6))

# A manipulação de listas é muito parecida com a de strings

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

lista = list(range(1, 5))

print(lista[::])  # Imprime todos os elementos
print(lista[2::])  # Imprime os elementos a partir de 2
print(lista[:2:])  # Imprime os elementos até o índice (2-1)

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

print(lista)
print(type(lista))
lista = tuple(lista)
print(lista)
print(type(lista))

# Desempacotamento de listas
lista = list(range(1, 4))

# tem que ser exatamente o mesmo número de elementos e do tamanho da lista
n1, n2, n3 = lista

print(n1)
print(n2)
print(n3)
# Shallow Copy e Deep Copy

# Forma 1 - Deep Copy
# após o .copy() as listas ficam independentes
# isso é chamado de Deep Copy (cópia profunda)
lista = list(range(1, 4))
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# Forma 2 - Shallow Copy
# apenas utilizando a atribuição, as duas listas continuam
# conectadas, e uma modificação implica-se às duas
# isso é chamado de Shallow Copy (Cópia Rasa)
lista = list(range(1, 4))
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

"""


