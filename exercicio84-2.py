grupo = list()
pessoas = list()
pesomaior = pesomenor = 0
nomemaior = nomemenor = ''
while True:
    quantidade = int(input('Quantas pessoas deseja cadastrar? '))
    for i in range(0, quantidade):
        pessoas.append(str(input('Nome: ')))
        pessoas.append(float(input('Peso: ')))
        if len(grupo) == 0:
            pesomaior = pesomenor = pessoas[1]
        else:
            if pessoas[1] > pesomaior:
                pesomaior = pessoas[1]
                nomemaior = pessoas[0]
            if pessoas[1] < pesomenor:
                pesomenor = pessoas[1]
                nomemenor = pessoas[0]
        grupo.append(pessoas[:])
        pessoas.clear()
    continuar = str(input('Deseja continuar? [s/n] ')).lower()[0]
    while continuar not in 'sn':
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
        continuar = str(input('Deseja continuar: [s/n] ')).lower()[0]
    if continuar == 'n':
        break
print(f'A pessoa mais pesada pesa:{pesomaior}kg e se chama {nomemaior}')
print('-' * 30)
print(f'A pessoa mais leve pesa:{pesomenor}kg e se chama {nomemenor}')
print('-' * 30)
print(f'O total de pessoas cadastradas foram {len(grupo)}.')
