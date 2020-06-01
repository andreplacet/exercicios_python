pessoas = list()
pesomaior = pesomenor = totalpessoas = 0
nomemenor = nomemaior = ''
while True:
    pessoas.append(str(input('Nome:')))
    pessoas.append(str(input('Peso: ')))
    continuar = str(input('Deseja continuar? [s/n] ')).lower()[0]
    totalpessoas += 1
    while continuar not in 'sn':
        print('VALOR INVALIDO, DIGITE NOVAMENTE!')
        continuar = str(input('Deseja continuar? [s/n] '))
    if continuar == 'n':
        break
for c in range(0, len(pessoas), 2):
    if c == 0:
        pesomaior = pesomenor = pessoas[c + 1]
        nomemaior = nomemenor = pessoas[c]
    if pessoas[c + 1] > pesomaior:
        pesomaior = pessoas[c + 1]
        nomemaior = pessoas[c]
    else:
        pesomenor = pessoas[c + 1]
        nomemenor = pessoas[c]
print(f'O total de pessoas cadastradas é {totalpessoas}.')
print(f'A pessoa mais pesada é {nomemaior} e pesa {pesomaior}.')
print(f'A pessoa mais leve é {nomemenor} e pesa {pesomenor}')
