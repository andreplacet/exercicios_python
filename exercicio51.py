'''n = int(input('Digite um número: '))
r = int(input('Indique a razão: '))
for i in range(n, 100, r):
    print(i)'''
num = int(input('Digite um número: '))
razao = int(input('Indique a razão: '))
decimo = num + (10 - 1) * razao
for c in range(num, decimo + razao, razao):
    print(c)
print('its over bitch!')
