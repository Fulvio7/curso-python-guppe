"""
16- Faça uma função chamada DesenhaLinha. Ela deve desenhar uma linha
na tela usando vários símbolos de igual '='. A função recebe por
parâmetro quantos sinais de igual serão mostrados.
Exemplo:
entrada: 4 -> saída: ====
"""


def desenha_linha(tamanho):
    print('=' * tamanho)


print('Desenha linha')
tam = int(input('Digite o tamanho da linha: '))

desenha_linha(tam)





