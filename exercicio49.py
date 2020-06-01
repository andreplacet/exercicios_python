n = int(input('Digite um número para imprimir sua Taboada: '))
for c in range(0, 11, 1):
    m = (n * c)
    print('{} x {} = {}'.format(n, c, m))
