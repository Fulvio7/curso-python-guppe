"""
22- Leia a idade e o tempo de serviço de um trabalhador e verifique
se ele pode ou não se aposentar. Para se aposentar, as condições
são as seguintes:
- Ter pelo menos 65 anos;
- Ou ter trabalhado pelo menos 30 anos;
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos;
"""

print('=== INSS ===')
idade = int(input('Digite a idade do trabalhador: '))
tempo = int(input('Digite o tempo de trabalho: '))

if (idade >= 65) or (tempo >= 30) or (idade >= 60 and tempo >= 25):
    print('Parabéns o senhor(a) já pode se aposentar! ')
else:
    print('Infelizmente o senhor(a) não pode se aposentar.')


