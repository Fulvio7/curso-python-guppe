
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

i = 0
while (i < 1) or (i > 1000):
    i = int(input('Digite um nº inteiro entre 1 e 1000: '))

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
        numeros_por_extenso += num[centena] + ' e '
    if dezena > 20:
        numeros_por_extenso += num[dezena] + ' e '
    if dezena < 20:
        numeros_por_extenso += num[i - centena]
    else:
        unidade = (i - centena - dezena)
    if unidade > 0:
        numeros_por_extenso += num[unidade]

print(f'Você digitou o nº {numeros_por_extenso}.')



