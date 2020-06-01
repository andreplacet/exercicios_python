viagem = float(input('\033[31mQual a distancia da viagem (em KM):\033[m'))
print('\033[7;30mViagens até 200km custam R$0,50 por km\033[m')
print('\033[7;30mViagens acima 200km custam R$0,45 por km\033[m')
if viagem <= 200:
    preco = viagem * 0.50
    print('\033[;31mA viagem irá custar \033[mR${:.2f}'.format(preco))
else:
    preco = viagem * 0.45
    print('\033[;31mA viagem irá custar \033[mR${:.2f}\033[m'.format(preco))