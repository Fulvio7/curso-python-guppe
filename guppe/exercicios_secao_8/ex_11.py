"""
11- Elabore uma função que receba três notas de uma aluno como
parâmetros e uma letra. Se a letra for 'A', a função deve retornar a
média aritmética das notas do aluno; se for 'P', deverá calcular a média
ponderada, com pesos: 5, 3 e 2.
"""


def calcula_media(nota1, nota2, nota3, tipo_media):
    if tipo_media == 'A':
        media = (nota1 + nota2 + nota3) / 3
        return media
    elif tipo_media == 'P':
        media = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10
        return media
    return 'Erro inesperado.'


n1, n2, n3 = -1, -1, -1
tipo_de_media = str

print('Média de um aluno:')

while n1 < 0 or n1 > 10:
    n1 = float(input('Digite a nota 1: '))

while n2 < 0 or n2 > 10:
    n2 = float(input('Digite a nota 2: '))

while n3 < 0 or n3 > 10:
    n3 = float(input('Digite a nota 3: '))

print('Digite o tipo de Média:')
while tipo_de_media != 'A' and tipo_de_media != 'P':
    tipo_de_media = input('Aritmética [A] ou Ponderada [P]: ')
    tipo_de_media = tipo_de_media.upper()


print(f'Média = {calcula_media(n1, n2, n3, tipo_de_media):.2f}')
