lista1 = []
lista2 = []
lista3 = []
matriz = []
somapares = somacoluna = 0
for c in range(0, 3):
    lista1.append(int(input(f'Digite um valor para a [linha 0 coluna {c}]: ')))
matriz.append(lista1[:])
for i in range(0, 3):
    lista2.append(int(input(f'Digite um valor para a [linha 1 coluna {i}]: ')))
matriz.append(lista2[:])
for d in range(0, 3):
    lista3.append(int(input(f'Digite um valor para a [linha 2 coluna {d}]: ')))
matriz.append(lista3[:])
for num in matriz:
    print(f'[ {num[0]} ] [ {num[1]} ] [ {num[2]} ]')
for par in matriz:
    for j in range(0, len(par)):
        if par[j] % 2 ==0:
            somapares += par[j]
for colunaum in matriz:
    somacoluna += colunaum[2]
print('-=' * 20)
print(f'A soma de todos os valores pares é: {somapares}')
print(f'A soma dos valores da terceia coluna é: {somacoluna}')
print(f'O maior valor da segunda linha é {max(lista2)}')
print('-=' * 20)
print('\033[33mFinalizado com Sucesso!\033[m')