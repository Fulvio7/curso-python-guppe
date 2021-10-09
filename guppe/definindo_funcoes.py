"""
Definindo Funções
São pequenos trechos de código que realizam tarefas específicas.
Pode ou não receber parâmetros.
Quando não retornam o resultado, as funções são chamadas de procedimentos.
Algumas funções possuem tipos de dados específicos.
Partem do princípio DRY - Don't Repeat Yourself (Não repita a si mesmo):
para simplificar a escrita de um código e sem repetições.

Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_da_entrada):
  bloco_da_funcao

Onde:
nome_da_funcao -> SEMPRE com letras minúsculas, e se for composto,
separado por underline (Snake Case).

parametros_de_entrada -> são opcionais, e separados por vírgula.

bloco_da_funcao -> corpo da função ou implementação, onde o processamento
é realizado, podendo ou não ter um retorno.

Utilizamos a palavra reservada 'def' para definir uma função.
Lembre-se sempre dos dois pontos :.
Lembre-se também de colocar duas linhas antes e depois de uma função.
"""

# Definindo a primeira função
# Exemplo 1


def diz_oi():
    print('Oi!')


"""
OBS:
1- Podemos utilizar outras funções dentro de uma função
2- A única tarefa desta função é imprimir 'Oi!'
3- Não recebe nenhum parâmetro de entrada
4- Não retorna nada
"""

# Utilizando funções
diz_oi()

"""
OBS: Sempre colocar parênteses para chamar a função
"""
# Exemplo 2


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida!')
    print('Viva o aniversariante!')


"""
for i in range(5):
    cantar_parabens()
"""

# Em Python, uma variável pode receber uma função
# Apesar de possível, isto não é usual
canta = cantar_parabens

canta()







