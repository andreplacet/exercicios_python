x = int(input('Digite o primeiro fator: '))
y = int(input('Digite o segundo fator: '))
while True:
    resposta = int(input('''[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NUMEROS
[5] - SAIR
: '''))
    if resposta == 1:
        soma = x + y
        print('A soma dos fatores é = {}'.format(soma))
    elif resposta == 2:
        multi = x * y
        print('A multiplicação dos fatores é = {}'.format(multi))
    elif resposta == 3:
        maior = x
        menor = x
        if x > y:
            maior = x
            menor = y
            print('O fator maior é {} e o menor é {}'.format(maior, menor))
        else:
            maior = y
            menor = x
            print('O fator maior é {} e o menor é {}'.format(maior, menor))
    elif resposta == 4:
        print('Digite novos valores')
        x = int(input('Digite o primeiro fator: '))
        y = int(input('Digite o segundo fator: '))
    elif resposta == 5:
        break
    if resposta not in (1, 2, 3, 4, 5):
        print('\033[31mValor invalido, tente novamente\033[m')
print('Voce saiu do programa!')
