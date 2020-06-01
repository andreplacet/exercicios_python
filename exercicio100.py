from time import sleep
from random import choice
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 31, 33, 32, 44, 50, 55, 56, 58, 61]
g = []


def sorteia(num):
    cont = 0
    print(f'Os números sorteados da lista {num} são:')
    while cont < 5:
        cont += 1
        n = [choice(num)]
        for i in n:
            g.append(i)
            print(i, end=' ')
            sleep(0.5)
    print()


def soma(s):
    soma = 0
    for j in range(0, len(s)):
        if s[j] % 2 == 0:
            soma += s[j]
    print(f'A soma dos valores pares da lista {s} é igual à: {soma}')


sorteia(numero)
soma(g)
