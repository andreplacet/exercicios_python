lista = []
listapares = []
listaimpares = []
for c in range(0, 7):
    lista.append(int(input(f'Digite o {c + 1} número: ')))
    if lista[c] % 2 ==0:
        listapares.append(lista[c])
    else:
        listaimpares.append(lista[c])
lista.clear()
lista.append(listapares[:])
lista.append(listaimpares[:])
print(lista)
print(f'Os valores pares em ordem crescente são: {sorted(listapares)}')
print(f'O valores ímpares em ordem crescente são: {sorted(listaimpares)}')
