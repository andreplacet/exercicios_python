while True:
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Informe seu Sexo [M/F]: ')).upper()
    if sexo not in 'MF':
        print('Valor de sexo digitado INVALIDO, tente novamente!')
    else:
        break
print('Cadastro Efetuado com sucesso!')