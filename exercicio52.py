num=int(input("Digite um numero: "))
if num % 2 == 1:
    print("o número {} é primo.".format(num))
else:
    print("o número {} não é primo.".format(num))

'''num1 = int(input('Digite um número: '))
total = 0
for c in range(1, num1 +1):
    if num1 % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num1, total))
if total == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele NÃO É PRIMO!')'''