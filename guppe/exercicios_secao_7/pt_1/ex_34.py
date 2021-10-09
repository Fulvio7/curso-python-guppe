"""
34- Leia 10 números diferentes e armazene-os em um vetor. Repita
a inserção até o usuário informar um número que não exista no vetor.
Ao final imprima o vetor preenchido.
"""
vetor, num = [], int()

print('Preencha o vetor')
while len(vetor) < 10:
    if len(vetor) == 0:
        vetor.append(int(input(f'v[{len(vetor)}] = ')))
    else:
        while num in vetor:
            num = int(input(f'v[{len(vetor)}] = '))
        vetor.append(num)

print(vetor)




