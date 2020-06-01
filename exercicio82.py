lista1 = list()
listapar = list()
listaimpar = list()
c = 0
while True:
    fim = int(input('Quantos numeros deseja adicionar na lista? '))
    for c in range(0, fim):
        lista1.append(int(input('Digite um numero para '
                                'adicionar à lista: ')))
        if lista1[c] % 2 == 0:
            listapar.append(lista1[c])
        else:
            listaimpar.append(lista1[c])
    continuar = str(input('Deseja continuar? [s/n] ')).lower()[0]
    while continuar not in 'sn':
        print('VALOR INVALIDO, TENTE NOVAMENTE')
        continuar = str(input('Deseja continuar? [s/n] ')).lower()[0]
    if continuar == 'n':
        break
    if continuar == 's':
        pass
print(lista1)
print(listapar)
print(listaimpar)