"""
19- Faça uma função que retorne o maior fator primo de um número.
"""


def maior_fator_primo(n):
    fatores = []
    fator = 2

    while n > 1:
        while n % fator == 0:
            fatores.append(fator)
            n /= fator
        fator += 1
        if fator * fator > n:
            if n > 1:
                fatores.append(fator)
                break

    return max(fatores)


print(maior_fator_primo(12))

