'''
help(print())

help(input()) # as duas maneiras executam a mesma documentação
print(input.__doc__)


Docstring

def contador(inicio, fim, passo):
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

def contador(i, f, p):
    """
    Faz uma contagem com inicio, fim e o passo
    :param i: a variável de inicio da contagem
    :param f: a variável para o fim da contagem
    :param p: a variável para o passo da contagem (determina o intervalo entre os valores da contagem)
    :return: NO RETURN
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


contador(0, 100, 10)

help(contador)
'''


def soma(a, b, c=0):# def soma(a=0, b=0, c=0) -> todas a variáveis podem ser opcionais
    """
    função para somar trê valores (ou variáveis)
    :param a: primeira vareável para soma
    :param b: segunda variável para soma
    :param c: terceira variável para soma
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')


# help(soma)
soma(2, 3, 5)
soma(3, 2)
soma(5, 6)


