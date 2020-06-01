print()
print('\033[31mB a n c o Ú n i c o\033[m')
print('\033[33m-\033[m'*50)
print('Contratação de Financiamento Imobiliario')
nome = str(input('Qual o seu nome? ')).strip()
valor = float(input('Qual o valor do imovel que deseja financiar? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao = valor / (anos * 12)
resultadosalario = salario*0.30
if prestacao >= resultadosalario:
    print('Sinto muito {}, infelizmente seu financiamento foi \033[31mNEGADO\033[m!'.format(nome.capitalize()))
else:
    print('Parabéns Senhor {}, seu financiamento foi \033[31mAPROVADO\033[m!'.format(nome.capitalize()))