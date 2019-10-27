aluguel = int(input('Quantos dias de locação?: '))
km = float(input('Quantos KM rodados?: '))
alugueltotal = aluguel * 60
kmtotal = km * 0.15
resultado = alugueltotal + kmtotal
print('O valor total pela locação foi de {:.2f} reais.'.format(resultado))