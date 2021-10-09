"""
Funções com Parâmetro Padrão (Default Parameters)

São aquelas onde a passagem de parâmetro é opcional.
Valores padrão:
- Nos permitem ser mais flexíveis nas funções
- Evita erros com parâmetros incorretos
- Nos permitem trabalhar com exemplos mais legíveis de código


# Exemplo
print('Patati Patata')
print()

# Exemplo de erro TypeError


def quadrado(numero):
    return numero**2


print(quadrado(7))
print(quadrado())



def exponencial(numero, potencia=2):  # neste caso 2 é padrão do paramêtro
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # Por padrão eleva ao quadrado
print(exponencial(3, 5))  # Eleva pela potência informada

# Obs: os parâmetros que possuírem valor padrão TEM de ser os ÚLTIMOS
# parâmetros da função

# Outro exemplo


def mostra_informacao(nome='Fúlvio', instrutor=False):
    if nome == 'Fúlvio' and instrutor:
        return 'Bem-vindo instrutor Fúlvio'
    elif nome == 'Fúlvio':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))


# Podemos trabalhar com qualquer tipo de dados
# Exemplo


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(2, 3))
print(mat(2, 3, subtracao))

# Devemos evitar utilizar variáveis locais, mas:

total = 0


def incrementa():
    global total  # 'global' nos permite utilizar a variável global 'total'

    total += 1
    return total


for i in range(5):
    print(incrementa())

"""

# Apesar de não ser usual, pode ocorrer de termos uma função declarada
# dentro de outra


def fora():
    contador = 0

    def dentro():
        # 'nonlocal' não é local nem global, mas do nível anterior
        nonlocal contador

        contador += 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

# print(dentro())  # NameError, função não encontada


