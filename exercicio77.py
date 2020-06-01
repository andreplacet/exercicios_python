palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PHYTON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for posicao in palavras:
    print(f'\nNa palavra {posicao} temos as vogais = ',end='')
    for letra in posicao:
        if letra.lower() in 'aeiou':
            print(f'\033[33m{letra}\033[m', end=' ')