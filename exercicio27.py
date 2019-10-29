nome = str(input('Qual seu nome completo? ')).strip()
n = nome.split()
print('Muito prazer em te conhecer {}'.format(n[0]))
print('Seu Ultimo nome é {}'.format(n[len(n)-1]))
