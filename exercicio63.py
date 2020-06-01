n = int(input('Quantos termos voce gostaria de mostrar? '))
x = 0
y = 1
cont = 1
while cont <= n:
  z = x + y
  x = y
  y = z
  cont += 1
  print(' -> \033[31m{}\033[m'.format(z),end='')
print('\nFIM')


'''anterior = 0
proximo = 0
n = int(input('Digite um numero: '))
while proximo < n:
  print(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior
  if(proximo == 0):
    proximo = proximo + 1'''