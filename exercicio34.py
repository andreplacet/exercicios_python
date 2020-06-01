salario = float(input('Qual o salário do funcionario? R$ '))
if salario >= 1250.00:
    resutado = salario * 1.10
if salario < 1250.00:
    resutado = salario * 1.15
print('O salario atual com aumento do funcionario é {:.2f}'.format(resutado))
