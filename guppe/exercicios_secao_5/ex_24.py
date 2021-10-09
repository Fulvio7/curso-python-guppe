"""
24- Leia um valor e o estado de destino, acrescente o juros e imprima
o valor final. Se o estado não estiver na lista a seguir mostre um erro:
MG 7%, SP 12%, RJ 15%, MS 8%.
"""

impostos = {'MG': 1.07, 'SP': 1.12, 'RJ': 1.15, 'MS': 1.08}

estado_venda = (input('Digite o estado da venda: ')).upper()

if estado_venda not in impostos:
    print(f'Erro: Estado {estado_venda} não está cadastrado.')
else:
    valor_produto = float(input('Digite o valor do produto: R$ '))
    preco_final = valor_produto * impostos[estado_venda]
    print(f'O preço final do produto é R$ {preco_final:.2f}')
