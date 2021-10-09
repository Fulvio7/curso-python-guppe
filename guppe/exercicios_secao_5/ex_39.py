"""
39- Faça um programa que leia o valor do salário de um funcionário
e o seu tempo (em anos) nesta empresa. Utilize as tabelas a seguir:
SALÁRIO ATUAL REAJUSTE
<= 500          25%
<= 1000         20%
<= 1500         15%
<= 2000         10%
> 2000          Sem reajuste

TEMPO       BÔNUS
< 1         Sem bônus
>= 1 <= 3   100
>= 4 <= 6   200
>= 7 <= 10  300
> 10        500
"""

print('=== FESTA DE FINAL DE ANO ===')
sal_atual = float(input('Digite o sálário atual: R$ '))
tempo = int(input('Digite quanto anos tem de empresa: '))
sal_final = sal_atual

# reajuste
reajuste = True
if sal_atual <= 500:
    sal_final = sal_atual * 1.25
elif sal_atual <= 1000:
    sal_final = sal_atual * 1.20
elif sal_atual <= 1500:
    sal_final = sal_atual * 1.15
elif sal_atual <= 2000:
    sal_final = sal_atual * 1.10
else:
    reajuste = False

# bônus
bonus = True
if tempo < 1:
    bonus = False
elif tempo <= 3:
    sal_final = sal_final + 100
elif tempo <= 6:
    sal_final = sal_final + 200
elif tempo <= 10:
    sal_final = sal_final + 300
elif tempo > 10:
    sal_final = sal_final + 500

if not reajuste and not bonus:
    print('Sem direito a aumento.')
else:
    print(f'Salário reajustado: R$ {sal_final:.2f}')



