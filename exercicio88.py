from time import sleep
from random import randint
jogo = []
final = []
num = randint(0, 60)
print('-' * 35)
print(f'{"JOGO DA MEGA-SENA":^35}')
print('-' * 35)
jogos = int(input('Quantos jogos voce quer que eu sortei? '))
print(f'-=-=-=-= Sorteando {jogos} =-=-=-=-=-')
for c in range(0, 6):
    if num not in jogo:
        jogo.append(num)
    else:
        pass
    final.append(jogo)
for sorteio in range(0, jogos):
    print(f'Jogo {sorteio + 1}: {final}')
    sleep(1)
print(f'{"Boa Sorte":-^35}')

'''from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos voce que sortear? '))
total = 1
cont = 0
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
    sleep(1)'''
