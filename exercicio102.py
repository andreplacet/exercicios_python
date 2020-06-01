'''
Crie um programa que tenha um função de nome fatorial(), que receba dois parametros: o primeiro que indique o número a calcular
e o outro paramêtro denominado 'show', que sera um valor lógico(booleana) e opcional indicando se será mostrado ou não
o processo de calculo no programa.
'''


def fatorial(n=1, show=False):
    """
    --> Calcula o fatorial de um númemero.
    :param n: o número a ser calculado o fatorial
    :param show: determina se o precesso sera impresso junto ao valor ou não (opcional)
    :return: O valor do fatorial de um número (n)
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show:    # por padrão o valor de show é Flase, não é necessario declarar "if show == True:"
        for d in range(n, 0, -1):
            print(f'{d} x ', end='')
        print(f, end=' ')
        print()
    else:
        print(f)


fatorial(5, show=True)
#print()
fatorial(4)
print()
help(fatorial)
