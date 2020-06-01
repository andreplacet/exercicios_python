from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
com = randint(0, 2)
print('''Sua opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 10)
print('O computador escolheu {}'.format(itens[com]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 10)
if com == 0:  # pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Invalida!')
elif com == 1:  # papel
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Invalida!')
elif com == 2:  # tesoura
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Computador Vence!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida!')
