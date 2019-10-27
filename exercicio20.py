from random import shuffle
aluno = str(input('Primeiro nome: '))
aluno2 = str(input('Segundo Nome: '))
aluno3 = str(input('Terceiro Nome: '))
aluno4 = str(input('Quarto Nome: '))
lista = [aluno, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação sera!')
print(lista)