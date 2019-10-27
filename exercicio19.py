from random import choice
aluno = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome de quarto aluno: '))
lista = [aluno, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))