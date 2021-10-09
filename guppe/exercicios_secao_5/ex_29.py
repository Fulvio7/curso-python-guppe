"""
29- Faça uma prova de matemática para crianças que estão aprendendo
a somar números inteiros menores do que 100. Escolha números aleatórios
entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b,
onde a e b são os números aleatórios. Peça a resposta. Faça cinco
perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.
"""

import random

parcela_a = list()
parcela_b = list()
soma_a_b = list()
resposta = list()
acertos = list()

print('=====  JOGO DA MATEMÁTICA  =====')
print('Qual a soma entre os dois números? ')

total_acertos = 0
total_erros = 0
for i in range(5):
    parcela_a.append(random.randint(1, 100))
    parcela_b.append(random.randint(1, 100))
    soma_a_b.append(parcela_a[i] + parcela_b[i])
    resposta.append(int(input(f'-> {parcela_a[i]} + {parcela_b[i]} = ')))

    if soma_a_b[i] == resposta[i]:
        acertos.append('Parabéns você acertou!')
        total_acertos += 1
    else:
        acertos.append(f'Errou. Você respondeu {resposta[i]}.')
        total_erros += 1

print('===== RESULTADO FINAL =====')
for i in range(5):
    print(f'-> {parcela_a[i]} + {parcela_b[i]} = {soma_a_b[i]} -> {acertos[i]}')

print(f'Total de acertos: {total_acertos}')
print(f'Total de erros: {total_erros}')
