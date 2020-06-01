frase = str(input('Digite um frase: ')).strip().split(' ')
frasesemespacos = ''.join(frase)
fraseinvertida = frasesemespacos[::-1]
if frasesemespacos == fraseinvertida:
    print('a frase \033[31m{}\033[m\nde tras pra frente é \033[33m{}\033[m\n\033[7mÉ um Palíndromo.\033[m'.format(frasesemespacos, fraseinvertida))
else:
    print('a frase \033[31m{}\033[m\nde trás pra frente é \033[33m{}\033[m\n\033[7mNÃO é um Palíndromo.\033[m'.format(frasesemespacos, fraseinvertida))
