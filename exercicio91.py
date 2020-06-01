from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}
ranking = {}
for chave, valor in jogo.items():
    print(f'O jogador {chave} escolheu {valor} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for p, v in enumerate(ranking):
    print(f'O {p + 1}º lugar:{v[0]} com {v[1]}')
    sleep(1)