#programa para adicionar, remover e imprimir listas
produtoepreco = []
print('-'*30)
print(f'{"INSERIR VALORES EM TABELAS .PY"}')
print('-'*30)
while True:
    opcao = int(input('''[1] INSERIR VALORES
[2] REMOVER VALORES
[3] IMPRIMIR VALORES
[4] SAIR
OPÇÃO: '''))
    while opcao not in (1, 2, 3, 4):
        print('\033[31mVALOR DIGITADO INVALIDO, TENTE NOVAMENTE!\033[m')
        opcao = int(input('''[1] INSERIR VALORES
[2] REMOVER VALORES
[3] IMPRIMIR VALORES
[4] SAIR
OPÇÃO: '''))
    if opcao == 1:
            produtos = int(input('Quantos produtos deseja adicionar? '))
            for contador in range(0, produtos):
                produtoepreco.append(int(input('Insira um valor '
                                       'númerico na lista: ')))
            while True:
                repetir = str(input('Deseja cadastrar um novo'
                            'valor? [s/n]')).lower()[0]
                if repetir in 's':
                    produtos = int(input('Quantos produtos deseja adicionar? '))
                    for contador in range(0, produtos):
                        produtoepreco.append(int(input('Insira um valor '
                                                       'númerico na lista: ')))
                elif repetir in 'n':
                    break
            while repetir not in 'sn':
                repetir = str(input('Valor invalido, Digite S ou N para '
                  'continuar!'))
    elif opcao == 2:
        try:
            produtoepreco.pop()
            print('O útimo valor inserido na lista foi removido')
        except:
            print('\033[33;41mVALORES AINDA NAO ADICIONADOS NA TABELA\033[m')
    elif opcao == 3:
        resposta = int(input('''[1] IMPIMIR VALORES
[2] IMPRIMIR VALORES EM ORDEM CRESCENTE
[3] IMPRIMIR VALORES EM ORDEM DECRESCENTE
[4] IMPRIMIR MAIOR
[5] IMPRIMIR MENOR
OPÇÃO '''))
        if resposta == 1:
            for v in produtoepreco:
                print(f'Os valores da lista são: {v}')
        elif resposta == 2:
            produtoepreco.sort()
            print(f'A lista em ordem crescente: {produtoepreco}')
        elif resposta == 3:
            produtoepreco.sort(reverse=True)
            print(f'A lista em ordem decrescente: {produtoepreco}')

    elif opcao == 4:
        print('Programa Finalizado com Sucesso!')
        break
