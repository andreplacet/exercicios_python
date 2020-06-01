from time import sleep


def contador(inicio, fim, passo):
    print(f'Contador de {inicio}, à {fim} em {passo}')
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
        sleep(0.5)
    if inicio > fim:
        for d in range(inicio, fim, -passo):
            print(f'{d}', end=' ')
            sleep(0.5)
    print('FIM', end='')
    print()


contador(1, 11, 1)
contador(10, 0, -1)
i = int(input('Inicio do contador: '))
f = int(input('Fim do contador:    '))
p = int(input('Passo do contador:  '))
if p == 0:
    p = 1
elif p < 0:
    p *= -1
contador(i, f, p)
