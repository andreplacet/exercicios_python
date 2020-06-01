s = 0
cont = 0
for n in range(0, 501, 3):
    if n % 2 == 1:
        cont = cont + 1
        s = s + n
print('A soma de todos os {} numeros ímpares e multiplos de 3,\nentre 0 e 500 são: {}'.format(cont, s))
