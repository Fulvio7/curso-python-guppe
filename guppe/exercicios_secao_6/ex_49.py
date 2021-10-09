"""
49- Carlos tem um colega de trabalho chamado João que recebe um terço
de seu salário. Carlos aplica seu salário na poupança (que rende 2% a.m.)
e João aplica seu salário num fundo de renda fixa (que rende 5% a.m.).
Mostre em quantos meses João iguala ou ultrapassa Carlos.
"""
carlos, mes, montante_carlos, montante_joao = 1, 1, 0, 0

joao = carlos / 3

while True:
    montante_carlos = carlos * (1.02 ** mes)
    montante_joao = joao * (1.05 ** mes)
    if montante_carlos <= montante_joao:
        print(f'joão alcança carlos depois de {mes} meses.')
        break
    mes += 1

