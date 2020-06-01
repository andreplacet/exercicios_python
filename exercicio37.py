print()
print('C o n v e r s o r d e B a s e')
print('\033[33m-\033[m'*50)
numero = int(input('Digite um número inteiro para converter sua base! '))
decisao = int(input('Escolha:\n1 - p/ binário\n2 - p/octal\n3 - p/hexadeciaml:\nSua escolha! '))
if decisao == 1:
    print('{} em binário é {}'.format(numero, bin(numero)[2:]))
elif decisao == 2:
    print('{} em octal é {}'.format(numero, oct(numero)[2:]))
elif decisao == 3:
    print('{} em hexadecimal é {}'.format(numero, hex(numero)[:2]))
else:
    print('Digite uma opção valida!')
