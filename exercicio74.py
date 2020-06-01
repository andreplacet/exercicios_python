from random import randint
cont = 0
a = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

print(f'O valores sorteados foram : {a[0]} {a[1]} {a[2]} {a[3]} {a[4]}')
print(f'Os Valores em ordem crescente: {sorted(a)}')
print(f'O maior valor foi {sorted(a)[0]}')
print(f'O menor valor foi {sorted(a)[4]}')