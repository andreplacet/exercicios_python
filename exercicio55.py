pesomaior = 0
pesomenor = 0
for i in range(0, 5):
    peso = float(input('Digite o peso: '))
    if i == 0:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('Peso maior {}'.format(pesomaior))
print('Peso menor {}'.format(pesomenor))
