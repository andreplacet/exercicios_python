def ajuda(com):
    titulo(f'acessando o manual de comando {com}', 2)
    print(c[3], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='')


c = ('\033[m', # 0 - sem cores
     '\033[0;30;41m', # 1 vermelho
     '\033[7;33;40m',  # 2 amarelo
     '\033[7;30m' # 3 branco
     )
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou comando: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)

