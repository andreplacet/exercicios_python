nome = str(input('Qual é o seu nome? ')).strip().upper()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='André':
    print('Seu nome é bem Popular no Brasil!')
elif nome in 'ANA RENATA FERNANDA RAFAELA GIULA':
    print('Lindo nome Femininos!')
print('Tenha um bom dia, \033[31m{}\033[m!'.format(nome.capitalize()))