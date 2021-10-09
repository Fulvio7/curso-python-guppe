"""
Module Collections - Deque

Deque é uma lista de alta performance.
"""

# Importando
from collections import deque
# Criação
deq = deque('geek')
print(deq)

# Adicionando elementos
deq.append('y')  # adiciona no final
print(deq)

deq.appendleft('k')  # adiciona no começo da lista
print(deq)

# Removendo elementos
print(deq.pop())  # remove e retorna o último elemento
print(deq.popleft())  # remove e retorna o primeiro elemento
print(deq)



