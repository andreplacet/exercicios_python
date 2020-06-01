from datetime import date
atual = date.today().year
s = 0
for c in range(0, 7, 1):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = atual - ano
    if idade >= 18:
        idade = 1
        c = idade
        s = (s + c)
    else:
        idade = 0
print('O número de pessoas maiores de 18 anos são: {}'.format(s))
