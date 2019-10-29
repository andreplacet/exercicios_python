nome = str(input('Qual o seu nome completo? ')).strip().upper()
print('A letra "A" aparece {} vezes na frase.'.format(nome.count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A ultima letra "A" apareceu na posição {}'.format(nome.rfind('A')+1))

