contador = soma = maior = menor = 0
resp = ''
while True:
    n = int(input('Digite um número: '))
    contador += 1
    soma += n
    media = soma / contador
    resp = str(input('Deseja adicionar mais valores? [s/n]: ')).lower()
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if resp in 'n':
        print('\033[33m --- Programa finalizado --- \033[m')
        break
    else:
        if resp not in 'sn':
            print('valor invalido!')
print(f'A média aritimetica dos valores é igual à: {media}, o maior valor digitado foi [{maior}] e o menor [{menor}]')
