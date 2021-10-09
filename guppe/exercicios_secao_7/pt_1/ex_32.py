"""
32- Leia dois vetores inteiros x e y, cada um com 5 elementos.
Calcule e mostre os vetores resultantes em cada caso abaixo:
- Soma entre x e y: soma de cada elemento de x com elementos da mesma
posição de y;
- Produto entre x e y: multiplicação entre cada elemento de x com o
elemento da mesma posição em y;
- Diferença entre x e y: todos os elementos de x que não existam em y;
- Intersecção entre x e y: apenas os elementos que aparecem nos dois
vetores;
- União entre x e y: todos os elementos de x, e todos os elementos de
y que não estão em x.
"""

v1, v2, soma, produto = [], [], [], []

print('Preencha v1')
for i in range(5):
    v1.append(int(input(f'v1[{i}] = ')))

print('\nPreencha v2')
for i in range(5):
    v2.append(int(input(f'v2[{i}] = ')))

    soma.append(v1[i] + v2[i])
    produto.append(v1[i] * v2[i])

v1 = set(v1)
v2 = set(v2)

diferenca = v1.difference(v2)
uniao = v1.union(v2)
interseccao = v1.intersection()

print('\nResultados: ')
print(f'Soma entre elementos de mesma posição: \n{soma}')
print(f'Produto entre elementos de mesma posição: \n{produto}')
print(f'Diferença de x para y: \n{diferenca}')
print(f'União entre os vetores: \n{uniao}')
print(f'Intersecção entre os vetores: \n{interseccao}')


