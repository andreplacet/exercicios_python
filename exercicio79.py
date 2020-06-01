lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print(f'O número {num}, foi adicionado a lista '
              f'com sucesso!')
    else:
        print('Valor duplicado, valor \033[31mNÃO\033[m adicionado')
    repetir = str(input('Deseja continuar? [s/n]')).lower()[0]
    while repetir not in 'sn':
        print('\033[33;41mValor invalido, tente novamente!\033[m')
        repetir = str(input('Deseja continuar? [s/n]')).lower()[0]
    if repetir == 'n':
        break
lista.sort()
print(f'Os valores adicionados na lista em ordem '
      f'crescente são {lista}')