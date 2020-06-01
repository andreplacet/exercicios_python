'''from time import sleep
games = []
while True:
    games.append(str(input('Adicione um jogo a lista: ')).upper())
    continuar = str(input('Deseja continuar? [sim/não] ')).lower()[0]
    if continuar == 'n':
        break
while True:
    search = str(input('Qual vide-game deseja pesquisar? ').upper())
    print(f'{" BUSCANDO ":-^30}')
    sleep(1)
    if search in games:
        print(f'Achei o game {search}')
    else:
        print('Me desculpe, o game não se encontra na lista!')
    repeat = str(input('Deseja continuar? [sim/não] ')).lower()[0]
    if repeat == 'n':
        break
print(f'{"PROGRAMA FINALIZADO COM SUCESSO":-^30}')'''

games = ['play', 'xbox', 'nintendo wi']
busca = str(input('Pesquisa: '))
print(f'O produto foi encontrado {games.index(busca)}')