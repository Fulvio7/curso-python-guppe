"""
43- Escreva um programa de ajuda a vendedores.
A partir de um valor total lido, mostre:
- o total a pagar com 10% de desconto;
- o valor de cada parcela, em 3x sem juros;
- a comissão do vendedor, no caso da venda ser
a vista (5% sobre o valor com desconto);
- a comissão do vendedor, no caso da venda ser
parcelada (5% sobre o valor total);
"""
print('============ SISTEMA DOS VENDEDORES FELIZES ============')
valor_total = float(input('Digite o valor total da compra: R$ '))

valor_a_vista = valor_total * 0.9
parcela = valor_total / 3

print('Selecione a forma de pagamento: ')
print(f'[ 1 ] À vista -> R$ {valor_a_vista:.2f} (10% de desconto) ')
print(f'[ 2 ] À prazo -> 3x R$ {parcela:.2f} sem juros  ')
forma_pgto = int(input('Forma 1 ou 2 ? '))

comissao = 0

if forma_pgto == 1:
    comissao = 0.05 * valor_a_vista
elif forma_pgto == 2:
    comissao = 0.05 * valor_total
else:
    print('Erro: selecione a forma correta de pagamento.')

print(f'Comissão do vendedor R$ {comissao:.2f}')



