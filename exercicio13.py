salario = float(input('Qual é o salário do funcionario?R$: '))
novo = salario+(salario*15/100)
print('O funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
