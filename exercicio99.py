from time import sleep


def maior(num):
    ma = 0
    print('-=' * 22)
    print(f'O valores passados foram:', end=' ')
    for valores in num:
        print(f'{valores}', end=' ')
        sleep(0.3)
    print()
    print(f'O tamando da lista com valores passados é {len(num)}')
    sleep(0.8)
    for i in range(0, len(num)):
        if i == 0:
            ma = num[i]
        else:
            if num[i] > ma:
                ma = num[i]
    print(f'O maior valor informado foi {ma}')


lista = [2, 3, 4, 5, 7, 20]
lista2 = [43, 65, 12, 754, 87, 45]
lista3 = [1, 9, 22, 3]
maior(lista)
maior(lista2)
maior(lista3)
