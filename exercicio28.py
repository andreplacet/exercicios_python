'''import random
sorteio = [1, 2, 3, 4, 5]
escolhido = random.choice(sorteio)
num = int(input('Digite um numero de 1 à 5: '))
if num == escolhido:
    print('Parabéns o numero {} foi o escolhido, e você respondeu {}!'.format(escolhido, num))
else:
    print('Voce Errou!')'''

import random
computador = random.randint(1, 5) #FAZ O COMPUTADOR SORTEAR UM NUMERO DE 1 À CINCO
print('-=-=-=-=-=-=-'*5)
print('Vou pensar em um número entre 1 e cinco, tente acertar!...')
print('-=-=-=-=-=-=-'*5)
jogador = int(input('Digite um número de 1 à 5 para saber se acertou!! :'))
if jogador == computador:
    print('PARABÉNS ! Voce Acertou!')
else:
    print('GANHEI ! Você errou !')

'''from random import randint
from time import sleep
from termcolor import colored
pc = randint(0, 5)
print(colored('-=-', 'yellow') * 19)
print(colored('Vou pensar em um número entre 0 e 5. Tente adivinhar...', 'blue'))
print(colored('-=-', 'yellow') * 19)
resp = int(input('Em que número eu pensei? '))
print(colored('PROCESSANDO...', 'magenta'))
sleep(2)
if resp == pc:
    print(colored('PARABÉNS! Você conseguiu me vencer!', 'green'))
else:
    print(colored('GANHEI! Eu pensei no {} e não no {}.', 'red').format(pc, resp))'''