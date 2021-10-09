"""
Loop for

Loop -> estrutura de repetição
For -> uma dessas estruturas

C ou Java:
for(int i = 0; i < 10; i++){
    //execução do loop
}

Python:
for item in interavel:
    # execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
-String -> nome = 'Fúlvio Barichello'
-Lista -> lista = [0, 1, 2, 3]
-Range -> numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que tranformar em lista

# Exemplo 1: string
for letra in nome:
    print(letra)

# Exemplo 2: lista
for numero in lista:
    print(numero)

# Exemplo 3: range

range(valor_inicial, valor_final)
Obs: O valor_final não é inclusive
Ex: range(1, 10) imprime de 1 a 9

for numero in range(1, 10):
    print(numero)

Enumerate: cria uma tupla
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

# Quando não precisamos de um parâmetro, por exemplo
# descartando o índice com _ (underline)
for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[0])


qte = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qte + 1):
    num = int(input(f'Informe o valor {n}/{qte} : '))
    soma = soma + num
print(f'A soma é {soma}')

for letra in nome:
    print(letra, end='')  # não vai pular linha

tabela de unicodes
https://apps.timwhitlock.info/emoji/tables/unicode
"""

# original: U+1F60D
# modificado: U0001F60D
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)


