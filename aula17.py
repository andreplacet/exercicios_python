# lanche = ['Pizza', 'Sorvete', 'Suco', 'Hambuguer']
# lanche.append('cookie') - adiciona um valor ao final da lista
# lanche.insert(0, 'cookie') - aidiciona um valor na posição indicada nos parametros
#print(lanche)

# lanche = ['Pizza', 'Sorvete', 'Suco', 'Hambuguer']
# del lanche[3] - deleta o valor nao posição indicada na lista
# lanche.pop(3) - pode ser usado para apagar o ultimo elemento da lista, ou por parametro definido
# lanche.remove('Pizza') # remove pelo valor passado no parametro, pelo nome e nao por posição

'''num = [2, 5, 8, 9]
num[2] = 3
num.append(7)
num.insert(1, 0)
if 4 in num:
    num.remove(4)
else:
    print('Nao achei o numero 4')
num.sort() # num.sort(reverse=True) imprimi a lista invertida
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

quantidades = []
quantidades.append(1)
quantidades.append(2)
quantidades.append(3)
quantidades.insert(0, 0)
quantidades.append(4)
quantidades.sort(reverse=True)
for p, q in enumerate(quantidades):
    print(f'Os valores contidos na lista são: {q}, e seus '
          f'indices são {p}.')
print('\033[33mPrograma finalizado com sucesso!\033[m')
