"""
Dicionários dict
Em algumas linguagens de programação, os dicionários Python são
conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.
São representados por {} chaves

print({})

Tanto chave quanto valor podem ser de qualquer tipo de dado.
Chave e valor são separados por : dois pontos.

# Criação de dicionários
# Forma 1: mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2: menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos
# Forma 1: via chave
print(paises['br'])
# print(paises['ru'])  # KeyError

# Forma 2: via get
print(paises.get('eua'))
print(paises.get('ru'))  # None

russia = paises.get('ru')

if russia:
    print(f'Encontramos o país.')
else:
    print('Não encontramos o país.')

# Podemos definir um valor padrão, caso não seja encontrado um resultado
pais = paises.get('ru', 'Não encontramos')
print(pais)

# Podemos verificar se determinada chave existe num dicionário
print('br' in paises)
print('ru' in paises)  # não tem esse país
print('Estados Unidos' in paises)  # não tem essa chave


# Podemos utilizar qualquer tipo de dado como chave, inclusive:
# listas, tuplas, dicionários

localidades = {
    (35.6894, 139.692): 'Tóquio',
    (40.6643, -73.9385): 'Nova Iorque',
    (-23.5489, -46.6388): 'São Paulo'
}
print(localidades)
print(type(localidades))

# Adicionar elementos
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1: mais comum
receita['abr'] = 350
print(receita)

# Forma 2
receita.update({'mai': 500})
print(receita)

# Atualizar
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 500})
print(receita)

# Inserção e Atualização se dão da mesma forma
# Dicionários NÃO aceitam uma mesma chave para dois valores

# Remover dados de um dicionário
# Forma 1: mais comum
receita.pop('mar')
print(receita)
ret = receita.pop('fev')
print(ret)
# 1 - Em dict pop sempre tem a chave
# 2 - O valor desta chave é retornado ao usar pop '300'

# Forma 2
del receita['fev']
print(receita)

# Métodos em dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário
d.clear()
print(d)

# Copiando um dicionário para outro
# Forma 1: deep copy
novo = d.copy()  #
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2: shallow copy
novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

"""

# Forma não usual de criação de dict
outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# .fromkeys(iterável, valor)

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(5), 'novo')
print(veja)

