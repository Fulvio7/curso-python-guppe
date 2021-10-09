"""
35- Leia a e b que sejam menores que 10_000 e:
- Crie um vetor onde cada posição é um algarismo do número. A primeira
posição é o algarismo menos significante, e assim por diante;
- Crie um vetor que seja a soma de a e b, mas faça-o usando apenas
os vetores construídos anteriormente.
Dica: soma as posições correspndentes. Se a soma ultrapassar 10,
subtraia 10 do resultado e some 1 à proxima posição.
"""
a, b = -1, -1
vetor_a, vetor_b, soma = [], [], []

while a < 0 or a > 10_000:
    a = int(input('Digite o valor de A (entre 1 e 10.000): '))

while b < 0 or b > 10_000:
    b = int(input('Digite o valor de B (entre 1 e 10.000): '))

string_a = str(a)
string_b = str(b)

for i in range(1, len(string_a)+1):
    vetor_a.append(int(string_a[-i]))

for i in range(1, len(string_b)+1):
    vetor_b.append(int(string_b[-i]))

print(f'Vetor A: {vetor_a}')
print(f'Vetor B: {vetor_b}')

while len(vetor_a) < 5:
    vetor_a.append(0)

while len(vetor_b) < 5:
    vetor_b.append(0)

for i in range(5):
    if vetor_a[i] + vetor_b[i] < 10:
        soma.append(vetor_a[i] + vetor_b[i])
    else:
        soma.append((vetor_a[i] + vetor_b[i]) - 10)
        vetor_a[i+1] += 1

print(f'Soma entre Vetor A e B: {soma}')
