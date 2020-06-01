while True:
    n = int(input('Informe o número para imprimir a Tabuada! [\033[33;40mdigite 0 para sair do programa\033[m]\033[m: '))
    print('\033[31m-\033[m' * 25)
    if n < 0 or n == 0:
        break
    for c in range(0, 11):
        resultado = n * c
        print(f'''{n} X {c} = \033[31m{resultado}\033[m''')
    print('\033[31m-\033[m'*25)
print('Programa Finalizado com Sucesso!')
