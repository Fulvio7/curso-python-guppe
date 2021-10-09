"""
41- Leia a altura e o peso de uma pessoa, calcule seu IMC (através
da tabela abaixo) e mostre a sua classificação.
IMC	                CLASSIFICAÇÃO	    OBESIDADE (GRAU)
MENOR QUE 18,5	    MAGREZA	            0
ENTRE 18,5 E 24,9	NORMAL	            0
ENTRE 25,0 E 29,9	SOBREPESO	        I
ENTRE 30,0 E 39,9	OBESIDADE	        II
MAIOR QUE 40,0	    OBESIDADE GRAVE	    III
"""

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'IMC = {imc:.4f}. CLASSIFICAÇÃO: MAGREZA')
elif 18.5 <= imc < 25:
    print(f'IMC = {imc:.4f}. CLASSIFICAÇÃO: NORMAL')
elif 25 <= imc < 30:
    print(f'IMC = {imc:.4f}. CLASSIFICAÇÃO: SOBREPESO')
elif 30 <= imc < 40:
    print(f'IMC = {imc:.4f}. CLASSIFICAÇÃO: OBESIDADE')
else:
    print(f'IMC = {imc:.4f}. CLASSIFICAÇÃO: OBESIDADE GRAVE')
