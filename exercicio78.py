lista = list()
for valores in range(0, 5):
    lista.append(int(input('Digite os valores para '
                           'adicionar na lista: ')))
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado na lista foi {max(lista)}, na posição '
      f'{lista.index(max(lista))}')
print(f'O menor valor digitado na lista foi {min(lista)}, na posição '
      f'{lista.index(min(lista))}')
