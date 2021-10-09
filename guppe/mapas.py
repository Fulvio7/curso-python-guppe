"""
Mapas -> Conhecidos em Python como DICIONÁRIOS

São representados por {} chaves.

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave}: {receita[chave]}')

print(receita.keys())

for chave in receita.keys():  # forma pythonica!!!
    print(receita[chave])

# Acessando valores
print(receita.values())

for valor in receita.values():  # modo pythonico
    print(valor)

# Desempacotamento de dicionários
print(receita.items())

for chave, valor in receita.items():
    print(f'chave: {chave} e valor: {valor}')

"""

receita = {1: 100, 2: 250, 3: 400}
print(receita)


# Soma, máximo e mínimo: desde que sejam numéricos

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))

print(len(receita))

print(sum(receita.keys()))
print(max(receita.keys()))
print(min(receita.keys()))


