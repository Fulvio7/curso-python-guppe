"""
32- Leia o código e a quantidade de um lanche, conforme a tabela
abaixo. Calcule o valor a ser pago por aquele lanche e mostre:
PRODUTO         CÓD PREÇO
Cachorro Quente 100 1.20
Bauru Simples   101 1.30
Bauru com Ovo   102 1.50
Hamburger       103 1.20
Cheeseburguer   104 1.70
Suco            105 2.20
Refrigerante    106 1.00
"""
produtos = {100: 'Cachorro Quente',
            101: 'Bauru Simples',
            102: 'Bauru com Ovo',
            103: 'Hamburger',
            104: 'Cheeseburguer',
            105: 'Suco',
            106: 'Refrigerante'}

precos = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20,
          104: 1.70, 105: 2.20, 106: 1.00}

codigo = int(input('Digite o código do produto: '))

if codigo in produtos:
    qtde = int(input(f'Digite a quantidade de {produtos[codigo]}: '))
    valor_final = qtde * precos[codigo]
    print(f'O seu {produtos[codigo]} ficou em R$ {valor_final:.2f}.')
else:
    print('Erro: Código inválido.')



