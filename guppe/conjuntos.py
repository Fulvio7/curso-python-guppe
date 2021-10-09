"""
Conjuntos

- Conjuntos em qualquer outra linguagem de programação, estamos falando
à Teoria dos Conjuntos da Matemática.

No Python, os conjuntos são chamados de Sets.
Da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- Elementos não são acessados via índice (conjuntos não indexados)
- Elementos não guardam a ordem de criação

Conjuntos são bons para se utilizar quando precisamos armazenar
elementos mas não nos importamos com a ordenação deles. Quando não
precisamos nos preocupar com chaves, valores e itens duplicados.

Os Sets são referenciados em Python através de {} chaves.

Diferença entre Conjuntos (Set) e Mapas (Dict) em Python:
- Um dicionário tem chave/valor;
- Um conjunto tem apenas valor;

# Definindo um conjunto

# Forma 1:

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

print(s)
print(type(s))

# Conjuntos com valores repetidos não dão erro, são ignorados
# e não farão parte do conjunto

# Forma 2: mais comum

s = {1, 2, 4, 3, 5, 5}

print(s)
print(type(s))

# Não possuem valores duplicados, nem tem ordem
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Podemos misturar tipos de dados

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Iteração
for i in s:
    print(i)

# Utilidade
# Lista de Cidades de pessoas que visitaram um museu
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
           'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(len(cidades))

# quantas cidades distintas (únicas) tivemos?
print(len(set(cidades)))


# Adicionando elementos
s.add(4)
s.add(4)  # duplicidade não dá erro
print(s)

s = {1, 2, 3}
print(s)
# Revovendo elementos, nenhum valor é retornado
# Forma 1:
s.remove(3)  # 3 não é índice, mas o valor a ser removido
# s.remove(8)  # KeyError, pois não encontra o valor 8
print(s)

# Forma 2
s.discard(2)  # remove o valor 2
s.discard(2)  # não gera nenhum erro, caso não encontre o valor
print(s)

# Copiando um conjunto para outro
# Forma 1 Deep Cop

novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 Shallow Copy
print(s)
outro = s
outro.add(4)
print(outro)
print(s)

# Removendo todos os elementos
s.clear()
print(s)


# Métodos matemáticos de conjuntos
estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}

# Conjunto com estudantes únicos
# Forma 1: Union (recomendada)
unicos1 = estudantes_python.union(estudantes_java)
# ou unicos1 = estudantes_java.union(estudantes_python)
# {'Fernando', 'Júlia', 'Gustavo', 'Ana', 'Patrícia', 'Guilherme', 'Marcos', 'Pedro', 'Ellen'}
print(unicos1)

# Forma 2: Pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Conjunto de estudantes em ambos os cursos
# Forma 1: Intersection (recomendado)
ambos1 = estudantes_python.intersection(estudantes_java)
# {'Fernando', 'Júlia', 'Gustavo', 'Ana', 'Patrícia', 'Guilherme', 'Marcos', 'Pedro', 'Ellen'}
print(ambos1)

# Forma 2: E comercial &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Conjunto de estudantes de um curso que não estão no outro
# Difference
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
# {'Guilherme', 'Marcos', 'Ellen', 'Pedro'}
so_java = estudantes_java.difference(estudantes_python)
print(so_java)
# {'Gustavo', 'Fernando', 'Ana'}


s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""






