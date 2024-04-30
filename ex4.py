"""
Exercício 04
Preencha uma lista com 10 itens e verifique se ela é um palíndromo, ou seja, se ela é
igual quando lida da esquerda para a direita e da direita para a esquerda.
"""

from random import randint

lista = []

for i in range(0, 10):
    lista.append(randint(1, 10))


listaReversa = lista.copy()
listaReversa.sort(reverse=True)
lista.sort()

print(f'A lista {lista}', end='')

if lista == listaReversa:
    print(' é um palíndromo')
else:
    print(' não é um palíndromo')
