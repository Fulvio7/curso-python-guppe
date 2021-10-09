"""
Tipo String
Se está entre aspas ou apóstrofos é string

\n quebra de linha
print('Angelina \nJolie')

ou

nome = '''Angelina
Jolie'''
print(nome)

Utiliza-se '\' como caracter de escape

nome = 'Fulvio Belato'
# nome = ['F', 'u', 'l', 'v', 'i', 'o', ' ', 'B', 'e', 'l', 'a', 't', 'o']

print(nome.upper()) # Deixa o nome com caracteres maiúsculos
print(nome.lower()) # Deixa o nome com caracteres minúsculos

print(nome[0]) # Seleciona o primeiro caracter de nome
print(nome[0:6]) # Slice de string (último número menos 1)
print(nome[::-1]) # Inverte todos os caracteres de nome

print(nome.split()) # Agrupa o nome em partes de uma lista pelo caracter desejado
print(nome.split()[0]) # Seleciona a primeira palavra de nome

print(nome.replace('G', 'P') #troca todos os caracteres'G' por 'P'

"""