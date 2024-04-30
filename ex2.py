"""
Exercício 02
Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
A partir dessa lista, gere uma nova lista contendo apenas os números primos da lista.
"""

from random import randint

lista, primos, qnt_divs = [], [], 0

for i in range(0, 30):
    lista.append(randint(1, 50))

for p in lista:
    qnt_divs = 0
    for d in range(1, p+1):
        if p % d == 0:
            qnt_divs += 1
    if qnt_divs <= 2 and p != 1:
        primos.append(p)

print(f'Lista gerada: {lista}\n'
      f'Lista de números primos gerada: {primos}')
