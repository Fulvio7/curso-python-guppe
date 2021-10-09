"""
Recebendo dados do usuário
Input -> entrada de dados, sempre string
Cast -> conversão de um tipo de dado em outro
"""
# Exemplo mais moderno
nome = input("Qual é o seu nome? ")    # input = entrada
print(f"Seja bem-vindo(a) {nome} ")

idade = int(input("Qual a sua idade? "))

print(f"{nome} tem {idade} anos ")
print(f"{nome} você nasceu no ano de {2020 - idade}")

"""
# Exemplo moderno
nome = input("Qual é o seu nome? ")    # input = entrada
print("Seja bem-vindo(a) {0} ".format(nome))

idade = input("Qual a sua idade? ")

print("{0} tem {1} anos ".format(nome, idade))
"""

"""
# Exemplo antigo, Python 2
nome = input("Qual é o seu nome? ")    # input = entrada
print("Seja bem-vindo(a) %s " % nome)

idade = input("Qual a sua idade? ")

print("%s tem %s anos " % (nome, idade))
"""

