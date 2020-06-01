primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da Progressiva Aritimetica: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('\nQuantos termos voce quer mostrar a mais? '))
print('FIM')