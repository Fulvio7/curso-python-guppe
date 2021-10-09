"""
Decimal()
A maioria das linguagens de programação tem algum tipo numérico exato
para evitar problemas de arredondamento de pontos flutuantes .float().
No caso do Python, esse tipo é o Decimal, com precisão arbitrária.
Com ele, nossos cálculos ganharam a precisão necessária.
É importante sempre analisarmos se vale a pena utilizá-lo, pois tipos
exatos demandam mais tempo de processamento.
Essa questão não é exclusiva do Python, mas sim da computação e de
como ela lida com números de ponto flutuante.
No mais baixo nível, computadores funcionam com a diferença de dois
estados elétricos - ligado e desligado, verdadeiro e falso.
Daí temos o binário, o famoso 0 e 1, e é por conta desse sistema que
os computadores conseguem ser tão rápidos com algumas coisas.
Entretanto, utilizando o formato binário para os números de ponto
flutuante, os computadores não conseguem representar com precisão
exata algumas frações (como 0.98 e 0.1). Desse modo, esses números
são automaticamente arredondados para o mais próximo que se encaixe
na possibilidade do binário, o que resulta em um pequeno erro de
precisão.
"""

from decimal import Decimal

ganhos_julho = 99.91 * 5
gastos_julho = 110.1 * 3
print(ganhos_julho)
print(gastos_julho)


ganhos_julho = Decimal('99.91') * 5
gastos_julho = Decimal('110.1') * 3
print(ganhos_julho)
print(gastos_julho)
