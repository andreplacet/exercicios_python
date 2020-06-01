lista = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > max(lista):
        lista.append(num)
        print('Valor adicionado no final da lista!')
    elif num < lista[0]:
        lista.insert(0, num)
        print(f'O valor {num}, foi adicionado na lista'
              f', na posição 0')
    else:
        lista.insert(1, num)
        print(f'O valor {num}, foi adicionado na posição 1')
print('-='*30)
print(lista)