lista1 = []
lista2 = []
lista3 = []
matriz = []
for c in range(0, 3):
    lista1.append(int(input('Digite um valor para a posição ')))
matriz.append(lista1[:])
for i in range(0, 3):
    lista2.append(int(input('Digite um valor para a posição ')))
matriz.append(lista2[:])
for d in range(0, 3):
    lista3.append(int(input('Digite um valor para a posição ')))
matriz.append(lista3[:])
for num in matriz:
    print(f'[ {num[0]:^4} ] [ {num[1]:^4} ] [ {num[2]:^4} ]')
print('\033[33mFinalizado com Sucesso!\033[m')