"""
1- Faça um programa que possua um vetor A que armazene 6 números inteiros.
Execute os seguintes passos:
a- Atribua os valores 1, 0, 5, -2, -5, 7.
b- Armazene em uma variável inteira, a soma entre os valores das posições
A[0], A[1] e A[5] do vetor e imprima o resultado.
c- Modifique A[4], atribuindo o valor 100.
d- Mostre na tela cada valor de A, um em cada linha.
"""
# a
a = [1, 0, 5, -2, -5, 7]

# b
soma = a[0] + a[1] + a[5]
print(soma)

# c
a[4] = 100

# d
for i in a:
    print(i)




