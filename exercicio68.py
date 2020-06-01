from random import randint
com = randint(1, 2)
contador = 0
print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*15)
while True:
    jogador = str(input('Escolha \033[33mpar\033[m ou \033[33mimpar\033[m '))
    contador += 1
    if com == 1:
        com = 'impar'
    else:
        com = 'par'
    if jogador == com:
        print(f'Você ganhou!, voce precisou de {contador} tentativas')
        break
    else:
        print('Tente Novamente!')