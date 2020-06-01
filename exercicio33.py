num = int(input('Digite um valor '))
num2 = int(input('Digite outro valor '))
num3 = int(input('Digite outro valor '))
menor = num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3
maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitar foi {}'.format(maior))