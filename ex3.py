"""
Exercício 03
Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
A seguir solicite um número inteiro e multiplique todos os itens da lista por esse número.
"""

from random import randint

lista, novaLista = [], []

for i in range(0, 30):
    lista.append(randint(1, 50))

# novaLista = lista.copy()

print(f'Lista gerada: {lista}')
produto = int(input('Digite um número inteiro para multiplicar a lista: '))

for m in lista:
    novaLista.append(m * produto)

print(f'Nova lista multiplicada: {novaLista}')
