"""
53- Faça um programa para ler as dimensões de um terreno: comprimento (c)
e largura (l); e o preço do metro da tela (p). Imprima o custo para cercar
este mesmo terreno com a tela.
"""

lado_1 = float(input('Digite o comprimento do terreno em metros: '))
lado_2 = float(input('Digite a largura do terreno em metros: '))
preco_tela = float(input('Digite o preço do metro da tela: R$ '))

custo_cercar = lado_1 * lado_2 * preco_tela

print(f'Fica em R$ {custo_cercar:.2f} cercar todo o terreno.')


