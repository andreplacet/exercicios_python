alunos = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    continuar = str(input('Deseja continuar? [s/n] ')).lower()[0]
    while continuar not in 'sn':
        print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
        continuar = str(input('Deseja continuar? [s/n] ')).lower()[0]
    if continuar == 'n':
        break
print('-=' * 25)
print(f'{"No.": <5}', end=' ')
print(f'{"NOME":^5}', end=' ')
print(f'{"MEDIA":>5}')
print('-' * 25)
for p, a in enumerate(alunos):
    print(f'{p:<5}{a[0]:^5}{a[3]:>5}')
print('-' * 35)
while True:
    opcao = int(input('Mostrar as notas de qual aluno? (digite 999 para sair) '))
    if opcao == 999:
        break
    else:
        try:
            print('-' * 35)
            print(f'Notas do Aluno {alunos[opcao][0]}, são {alunos[opcao][1]}, {alunos[opcao][2]}')
            print('-' * 35)
        except:
            print(f'VALOR FORA DO ALCANE, FORAM CADASTRADOS APENAS {opcao} ALUNOS.')
            print('-' * 35)
print('FINALIZADO')
