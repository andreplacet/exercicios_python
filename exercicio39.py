'''nome = str(input('Qual o seu nome? '))
idade = int(input('Qual sua idade? '))
anoalistamento = 2019 - idade
if anoalistamento == 2001:
    print('{} já é hora de se alistar!'.format(nome.capitalize()))
elif anoalistamento > 2001:
    resultado = 18 - idade
    print('{} ainda falta(m) {} ano(s) para se alistar!'.format(nome.capitalize(), resultado))
elif anoalistamento < 2001:
    print('{} já passou o prazo para se alistar!'.format(nome.capitalize()))'''

from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano de nascimento? '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Voce ja deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi {}'.format(ano))