"""
38- Faça um programa que calcule o terno pitagórico a, b, c, para o qual
a + b + c = 1000. Um terno pitagórico é o conjunto de três números
naturais a, b, c, para a qual a**2 + b**2 = c**2.
Exemplo: 3**2 + 4**2 = 5**2  ->  9 + 16 = 25
"""
# Eu poderia utilizar while, mas acho que com for
# fica mais limpo e simples, porque sei que a, b e c
# não passarão de 1000
achou = False
for a in range(1, 1001):
    for b in range(1, 1001):
        for c in range(1, 1001):
            if ((a**2) + (b**2) == c**2) and (a + b + c == 1000):
                print('Resultado Final:')
                print(f'a = {a}, b = {b}, c = {c}')
                achou = True
            if achou:
                break
        if achou:
            break
    if achou:
        break
    print('Procurando...')

