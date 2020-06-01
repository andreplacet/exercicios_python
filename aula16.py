#lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim')
#print(lanche[1]) #mostra o indice da tupla na posição a partir de 0

#lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim')
#print(lanche[-2]) #inverte a lista de trás pra frente ate o indice desejado

#lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim')
#print(lanche[::-1])#imprimi a tupla invertida (de trás pra frente)

#lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim')
#print(lanche[1:3])

#lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim')
#print(lanche)#imprimi a tupla completa

#lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim')
#print(lanche[:2])

#lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim')
#print(lanche[:3])

#lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim')
#print(lanche[-2:])#impessão invertida, porem em ordem

lanche = ('hamburguer', 'Pizza', 'Suco', 'Pudim', 'batata')
    #print(lanche)
    #print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}, na posicão \033[31m{cont}\033[m')

print('\033[33m-\033[m'*30)

for pos, c in enumerate(lanche):
    print(f'EU vou comer {c}, na posição \033[31m{pos}\033[m')
print('Comi pra caramba!')

print(sorted(lanche)) #deixa em ordem alfabetica

