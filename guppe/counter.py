"""
Module Collections - Counter (Contador)

Collections -> High-performance container datatypes

Counter: Recebe um iterável como parâmetro e cria um objeto do
tipo collections.Counter, que é parecido com um dicionário:
a chave é o elemento do iterável e como valor a quantidade de
ocorrências daquele elemento.

# Importando o módulo
from collections import Counter
# Exemplo 1
# Podemos utiizar qualquer iterável
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 3, 5, 4, 42, 5, 12, 66, 1, 'k']

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)
# Counter({1: 6, 3: 4, 2: 3, 5: 2, 4: 1, 42: 1, 12: 1, 66: 1, 'k': 1})

# Exemplo 2
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""
# Importando o módulo
from collections import Counter

# Exemplo 3
texto = """Angelina Jolie (nascida Angelina Jolie Voight; Los Angeles,
4 de junho de 1975) é uma atriz, cineasta e ativista humanitária 
americana. Estreou no cinema ao lado de seu pai, Jon Voight, em 
Lookin' to Get Out (1982); porém, a carreira dela começou a sério 
uma década mais tarde, quando participou do filme de baixo orçamento 
Cyborg 2 (1993), seguido de seu primeiro papel principal em uma grande 
produção em Hackers (1995). Posteriormente, foi escalada para estrelar
os telefilmes biográficos George Wallace (1997), pelo qual ganhou seu
primeiro Prêmio Globo de Ouro de Melhor Atriz Coadjuvante em 
Televisão e recebeu uma indicação ao Prêmio Emmy do Primetime 
para Melhor Atriz Coadjuvante em minissérie ou telefilme, 
e Gia (1998), vencendo o novamente o Globo de Ouro, só que, 
desta vez, na categoria de Melhor Atriz em Minissérie ou Filme 
para Televisão. Em 1999, recebeu elogios por parte dos críticos 
especializados por sua interpretação como Lisa Rowe no filme Girl, 
Interrupted, pelo qual ganhou o Oscar de Melhor Atriz Coadjuvante.
"""
palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# As 5 palavras com mais ocorrências
print(res.most_common(5))
