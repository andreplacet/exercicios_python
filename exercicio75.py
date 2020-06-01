num = (int(input('Digite um Número: ')), int(input('Digite outro número: ')), int(input('Mais um número: ')), int(input('Ultimo número: ')))
print(f'Você digitou os valores {num}')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
else:
    print('O número 9 não apareceu nenguma vez!')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print('O número 3 não apareceu nenhuma vez!')
for par in num:
    if par % 2 == 0:
        print(f'Os valores pares digitados foram {par}')
