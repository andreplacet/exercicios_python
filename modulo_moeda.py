def metade(n, show=False):
    r = n // 2
    if show:
        j = r
        m = f'{j:.2f}'
        return m
    else:
        return r


def dobro(n, show=False):
    r = n * 2
    if show:
        j = r
        m = f'{j:.2f}'
        return m
    else:
        return r


def aumentar(n, ac=10, show=False):
    r = n + (n * (ac / 100))
    if show:
        j = r
        m = f'{j:.2f}'
        return m
    else:
        return r


def diminuir(n, dc=13, show=False):
    r = n - (n * (dc / 100))
    if show:
        j = r
        m = f'{j:.2f}'
        return m
    else:
        return r


def moeda(n):
    j = n
    return f'{j:.2f}'


def resumo(p, a=18, r=22):
    print('-' * 30)
    print(f'{"RESUMO DE VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado: ":<20}{moeda(p).replace(".", ","):<10}')
    print(f'{"O dobro do preço: ":<20}{dobro(p, show=True).replace(".", ","):<10}')
    print(f'{"Metado do preço: ":<20}{metade(p, show=True).replace(".", ","):<10}')
    print(f'{a}% de aumento:{aumentar(p, a, show=True).replace(".", ","):>11}')
    print(f'{r}% de desconto:{diminuir(p, r, show=True).replace(".", ","):>10}')
    print('-' * 30)
    return 'Compra Finalizada'


def leiadinheiro(txt):
    valido = False
    while not valido:
        i = str(input(txt).replace(',', '.').strip())
        if i.isalpha() or i == '':
            print('\033[31mINVALIDO, TENTE NOVAMENTE (APEPAS NUMEROS)\033[m')
        else:
            valido = True
            return float(i)
