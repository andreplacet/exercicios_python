lista = list()
while True:
    num = int(input('Quantos numeros deseja inserir na lista? '))
    for cont in range(0, num):
        lista.append(int(input('Digite um valor para inserir'
                               'na lista: ')))
    repetir = str(input('Deseja continuar? ')).lower()[0]
    while repetir not in 'sn':
        print('Valor invalido! Tente novamente')
        repetir = str(input('Deseja continuar? ')).lower()[0]
    if repetir == 'n':
        break
print(f'A quantidade valores digitados para a lista foi {len(lista)}')
lista.sort(reverse=True)
print(f'A lista de forma de decrescente {lista}')
if 5 in lista:
    print(f'O valor 5 foi impresso {lista.count(5)} vezes')
else:
    print('O valor cinco não foi encontrado!')