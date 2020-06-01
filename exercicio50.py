s = 0
for n in range(0, 6, 1):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s = s + num
    elif num % 2 == 1:
        num = 0
print('\033[31m{}\033[m'.format(s))
