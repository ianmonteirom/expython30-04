"""
Exercício 05
Preencha duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas
"""

from random import randint

lista1, lista2, lista3 = [], [], []

for i in range(0, 10):
    lista1.append(randint(1, 20))

for i in range(0, 10):
    lista2.append((randint(50, 100)))

lista3 = lista1 + lista2
lista3.sort()


print(f'Lista 1: {lista1}\n'
      f'Lista 2: {lista2}\n'
      f'Lista 3: {lista3}')
