contador = soma = 0
while True:
    n = int(input('Digite numero inteiros [digite 999 para terminar o programa]: '))
    if n == 999:
        break
    contador += 1
    soma += n
print('A quantidade de números digitados foram {}, e a soma deles é {}!'.format(contador, soma))