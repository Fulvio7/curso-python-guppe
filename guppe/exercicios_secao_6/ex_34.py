"""
34- Faça um programa que calcule o menor número divisível por cada
um dos números de 1 a 20.
Exemplo de 1 a 10 -> 2520 divide por 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
"""
num, tem_que_dar_20 = 0, 0
while tem_que_dar_20 < 20:
    num += 1
    tem_que_dar_20 = 0
    for i in range(1, 21):
        if num % i == 0:
            tem_que_dar_20 += 1
    print(num)

print(f'Resultado Final: {num}')

"""
Após uma hora e dez minutos de processamento
cheguei ao resultado!!! 
Resultado Final: 232792560
"""