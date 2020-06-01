while True:
    num = int(input('Digite um número: '))
    razao = int(input('Indique a razão: '))
    decimo = num + (10 - 1) * razao
    for c in range(num, decimo + razao, razao):
        print('\033[33m->{}\033[m'.format(c),end=' ')
    sair = str(input('\n\033[32mDeseja continuar?\033[m [s/n]')).lower()
    if sair == 'n':
        print('\033[31mPrograma finalizado!\033[m')
        break

