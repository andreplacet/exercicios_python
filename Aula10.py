'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')'''

nome = str(input('Digite seu nome: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n3)/3
print('A sua média foi {:.1f}'.format(m))
if m >= 5:
    print('Você foi aprovado {}!! Parabéns.'.format(nome))
else:
    print('{} você reprovado.'.format(nome))