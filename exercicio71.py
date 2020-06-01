nota = 50
print('='*25)
print('=====  BANCO ANDRE  =====')
print('='*25)
n = int(input('Qual valor deseja sacar? R$ '))
total = n
totalnotas = 0
while True:
    if total >= nota:
        total -= nota
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f'Total de {totalnotas} cédulas de R$:{nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnotas = 0
        if total == 0:
            break
