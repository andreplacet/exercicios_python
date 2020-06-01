def ficha(nome, g):
    '''
    --> Programa simples, feito para estudos, determina o nome de um jogador e quantos gols
    marcou no campeonato
    :param nome: Nome do jogador
    :param g: Quantidade de gols
    :return: NO RETURN
    '''
    print(f'O jogador {nome} marcou {g} gols no campeonato!')

try:
    jogador = str(input('Nome do Jogador: '))
    gol = int(input('Número de gols: '))
except ValueError:
    jogador = '<desconhecido>'
    gol = 0
ficha(jogador, gol)

print()
help(ficha)

