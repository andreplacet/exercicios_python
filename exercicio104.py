def leiaint(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('\033[31mERRO! Digite um múmero inteiro valido!\033[m')
        if ok: #Ok como padrão recebe False, não sendo necessario fazer a comparação (if ok == True) caso a condição seja satisfeita
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')
