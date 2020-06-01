'''
Crie um programa que tenha uma função chamada voto() que vai receber como paramêtro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto: NEGADO, OPCINAL ou OBRIGATORIO.
'''


def voto(a):
    from datetime import date
    idade = date.today().year - a
    if idade >= 18 and idade < 65:
        r = print(f'Voce tem {idade} anos e o voto é obrigatório!')
    elif idade > 14 and idade < 18 or idade > 65:
        r = print(f'Voce tem {idade} anos e o voto é opcional!')
    else:
        r = print(f'Você tem {idade} anos e menos que a idade permitida para votar, VOTO NEGADO')
        return r


nasc = int(input('Informe o ano de nascimento: '))
voto(nasc)
