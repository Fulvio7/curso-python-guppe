"""
40- Leia o custo de fábrica de um carro novo e calcule o custo do
consumidor. Utilize a tabela abaixo:
CUSTO DE FÁBRICA    COMISSÃO DISTRIBUIDOR   IMPOSTOS
<= 12000            5%                      isento
> 12000 <= 25000    10%                     15%
> 25000             15%                     20%
"""

custo_fabrica = float(input('Digite o valor de fábrica: R$ '))
custo_consumidor = float()

if custo_fabrica <= 12_000:
    custo_consumidor = custo_fabrica * 1.05
elif 12_000 < custo_fabrica <= 25_000:
    custo_consumidor = (custo_fabrica * 1.10) + (custo_fabrica * 1.15)
else:
    custo_consumidor = (custo_fabrica * 1.15) + (custo_fabrica * 1.20)

print(f'Custo do consumidor: R$ {custo_consumidor:.2f}')

