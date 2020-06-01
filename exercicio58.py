from random import randint
c = 0
while True:
    x = randint(1, 10)
    num = int(input('Digite um numero de 1 a 10 para tentar advinhar! '))
    c += 1
    if num < x:
        print('Hm, faltou pouco, tente numeros maiores que {}'.format(num))
    if num > x:
        print('Hm, passou um pouco haha, tente numeros menores que {}'.format(num))
    if num == x:
        print('Parabéns voce acertou o número sorteado que foi {}, e você precisou de {} tentativas'.format(x, c))
        break
    else:
        print('Voce errou, tente novamente!')
