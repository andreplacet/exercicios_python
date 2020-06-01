pessoas = dict()
grupo = list()
maiore_media = list()
total_mulheres = list()
soma = 0
print(f'\033[7;31m{"PROGRAMA CADASTRO: DICIONARIO E LISTAS": ^30}\033[m')
print('\033[33m-=\033[m' * 19)
while True:
    pessoas['nome'] = str(input('Nome: ').capitalize().strip())
    pessoas['idade'] = int(input('Idade:'))
    pessoas['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    while pessoas['sexo'] not in 'MF':
        print('VALOR INVALIDO, DIGITE "M" para masculino e "F" para feminino')
        pessoas['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    soma += pessoas['idade']
    continuar = str(input('Deseja continuar: [s/n] ')).lower()[0]
    grupo.append(pessoas.copy())
    while continuar not in 'sn':
        print('VALOR INVALIDO, DIGITE SIM OU NÃO PARA SAIR!')
        continuar = str(input('Deseja continuar: [s/n] ')).lower()[0]
    if continuar == 'n':
        break
media = soma / ((len(grupo)))
print('\033[33m-=\033[m' * 19)
for d in range(0, len(grupo)):
    if grupo[d]['idade'] > media:
        maiore_media.append(grupo[d]['nome'])
        maiore_media.append(grupo[d]['idade'])
    else:
        pass
    if grupo[d]['sexo'] == 'F':
        total_mulheres.append(grupo[d]['nome'])
    else:
        pass
print(f' - O grupo tem {len(grupo)} pessoas')
print(f' - A média de idade é de {media:.2f} anos')
print(f' - A mulheres cadastrasdas foram: ', end='')
for c in range(0, len(total_mulheres)):
    print(f'{total_mulheres[c]}', end=' ')
print()
print(f'A lista de pessoas com idade acima da média: ')
for j in range(0, len(maiore_media), 2):
    print(f'    Nome: \033[33m{maiore_media[j]}\033[m; idade: \033[33m{maiore_media[j + 1]}\033[m')
print('Programa encerrado com sucesso!')
