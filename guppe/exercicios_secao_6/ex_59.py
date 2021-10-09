"""
59- Leia o número de habitantes e o valor do kWh. Para cada habitante
leia o consumo do mês e o código do consumidor:
1-Residencial, 2-Comercial, 3-Industrial. No final imprima o maior,
o menor e a média do consumo dos habitantes; e por fim o total do consumo
de cada categoria de consumidor.
# Decidi remover o valor do kWh porque não o utilizo para nada...
"""

categorias = {1: 'Residencial', 2: 'Comercial', 3: 'Industrial'}

num_habs, valor_kWh, maior, menor, media = 0, 0, float(), float(), float()
total_consumo, tot_cate1, tot_cate2, tot_cate3 = 0, 0, 0, 0

while num_habs <= 0:
    num_habs = int(input('Digite o número de habitantes avaliados: '))
# while valor_kWh <= 0:
#     valor_kWh = float(input('Digite o valor do kWh: R$ '))

for i in range(1, num_habs+1):
    consumo_kWh, cate = -1, 0
    print(f'\nConsumidor {i}:')
    while consumo_kWh < 0:
        consumo_kWh = float(input('Digite o consumo [kWh]: '))
    while cate not in categorias:
        cate = int(input('Digite a categoria [1, 2 ou 3]: '))

    total_consumo += consumo_kWh
    if i == 1:
        maior, menor = consumo_kWh, consumo_kWh
    else:
        if maior < consumo_kWh:
            maior = consumo_kWh
        if menor > consumo_kWh:
            menor = consumo_kWh

    if cate == 1:
        tot_cate1 += consumo_kWh
    elif cate == 2:
        tot_cate2 += consumo_kWh
    elif cate == 3:
        tot_cate3 += consumo_kWh

print('\nResultados')
print(f'Maior consumo: {maior} kWh')
print(f'Menor consumo: {menor} kWh')
print(f'Média consumo: {total_consumo/num_habs} kWh')
print(f'\nPor categorias: ')
print(f'1-{categorias[1]}: {tot_cate1} kWh')
print(f'2-{categorias[2]}: {tot_cate2} kWh')
print(f'3-{categorias[3]}: {tot_cate3} kWh')






