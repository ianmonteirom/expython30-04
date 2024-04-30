"""
Exercício 01
Preencha uma lista com 10 números aleatórios únicos (sorteados de 1 a 20), ou seja,
sem elementos repetidos.
"""

from random import randint

aleatorios = []
cont = 1
while cont <= 10:
    n = randint(1, 20)
    if n not in aleatorios:
        aleatorios.append(n)
        cont += 1

aleatorios.sort()
print(f'Lista de números aleatórios: {aleatorios}')
