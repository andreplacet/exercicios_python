from math import factorial
while True:
    n = int(input('Digite o valor para fatorar, ou 0 para sair: '))
    if n == 0:
        break
    print('O fatorial de {} é {}'.format(n, factorial(n)))
print('Programa finalizado com sucesso.')


