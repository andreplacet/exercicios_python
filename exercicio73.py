tabelabrasileirao = ('0', 'Corinthians', 'Santos', 'São Paulo', 'Palmeiras', 'Havaí', 'Curitiba',
                     'Flamengo', 'Portuguesa', 'Vasco', 'Goias', 'Chapecoense', 'Atletico Paranaense',
                     'Sport', 'Bahia', 'Vitoria', 'Atletico Mineiro', 'Cruzeiro', 'Internacional', 'Gremio',
                     'Fluminense')
resp = ''
print('\033[30;43m---- MEU BRASILEIRÃO ---\033[m     ')
while True:
    while True:
        indice = int(input('''\033[33m[1]\033[m - IMPRIMIR O G5
\033[33m[2]\033[m - IMPRIMIR O Z5
\033[33m[3]\033[m - ORDEEM ALFABETICA
\033[33m[4]\033[m - SOLICITAR BUSCA DE TIME
OPÇÂO: '''))
        if indice not in (1, 2, 3, 4):
            indice = int(input('''\033[33m[1]\033[m - IMPRIMIR O G5
\033[33m[2]\033[m - IMPRIMIR O Z5
\033[33m[3]\033[m - ORDEEM ALFABETICA
\033[33m[4]\033[m - SOLICITAR BUSCA DE TIME
OPÇÂO: '''))
        else:
            break
    if indice == 1:
        print(f'A classificação do G5 é -> {tabelabrasileirao[1:5]}')
    elif indice == 2:
        print(f'A classificação do Z5 é -> {tabelabrasileirao[-5:]}')
    elif indice == 3:
        print(f'A Tabela em Ordem Alfabética é -> {sorted(tabelabrasileirao[1::])}')
    elif indice == 4:
        n = int(input('Digite a posição que deseja: '))
        print(f'O time que esta na {n}º posição do Brasileirão é o {tabelabrasileirao[n]}.')
    resp = str(input('Deseja Repetir a pesquisa? [S/N]: '))[0]
    if resp not in 'Ss':
        pass
    if resp in 'Nn':
        break
print('Programa Finalizado com Sucesso!')


