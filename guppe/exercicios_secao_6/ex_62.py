"""
62- Se os números de 1 a 5 são escritos em palavras: um, dois, três,
quatro, cinco, então há 21 letras usadas no total (2+4+4+6+5=21).
Faça um programa que conte quantas letras seriam utilizadas se todos
os números de 1 a 1000 fossem escritos em palavras.
Obs: Não conte espaços ou hífens.
"""

num = {0: '', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
       6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
       11: 'onze', 12: 'doze', 13: 'treze', 14: 'catorze',
       15: 'quinze', 16: 'dezesseis', 17: 'dezessete',
       18: 'dezoito', 19: 'dezenove', 20: 'vinte', 30: 'trinta',
       40: 'quarenta', 50: 'cinquenta', 60: 'sessenta',
       70: 'setenta', 80: 'oitenta', 90: 'noventa', 100: 'cento',
       200: 'duzentos', 300: 'trezentos', 400: 'quatrocentos',
       500: 'quinhentos', 600: 'seiscentos', 700: 'setecentos',
       800: 'oitocentos', 900: 'novecentos'}

numeros_por_extenso, centena, dezena, unidade = '', int(), int(), int()
for i in range(1, 1001):
    if i < 20:
        numeros_por_extenso += num[i]
    elif i == 100:
        numeros_por_extenso += 'cem'
    elif i == 1000:
        numeros_por_extenso += 'mil'
    else:
        centena = (i // 100) * 100
        dezena = ((i - centena) // 10) * 10
        unidade = 0
        if centena > 0:
            numeros_por_extenso += num[centena] + 'e'
        if dezena > 20:
            numeros_por_extenso += num[dezena] + 'e'
        if dezena < 20:
            numeros_por_extenso += num[i - centena]
        else:
            unidade = (i - centena - dezena)
        if unidade > 0:
            numeros_por_extenso += num[unidade]

print('Números de 1 a 1000 por extenso e sem separação:')
print(numeros_por_extenso)
print(f'Número total de caracteres: {len(numeros_por_extenso)}')

