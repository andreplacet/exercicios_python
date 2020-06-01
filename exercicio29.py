import termcolor
velocidade = float(input('Qual a velocidade atual do carro?( em Kilometros ) '))
multa = (velocidade - 80)*7
if velocidade <= 80:
    print (termcolor.colored('Tenha um bom dia! Dirija com segurança','blue' ))
else:
    print(termcolor.colored('MULTADO! Você excedeu o limite permitido que é de 80km, \nvocê deve pagar um multa de R${:.2f}!'.format(multa), 'red'))
