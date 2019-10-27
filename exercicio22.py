nome = str(input('Qual o seu nome? ')).strip()
print('Analisando seu Nome...')
print('Seu nome maisculo é {}.'.format(nome.upper()))
print('Seu nome minusculo é {}.'.format(nome.upper()))
print('Seu nome tem {} caracteres.'.format(len(nome)-nome.count(' ')))
print('Seu Primeiro Nome tem {} caracteres.'.format(nome.find(' ')))
primeironome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeironome[0], len(primeironome[0])))

