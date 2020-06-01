print('\033[33m-=\033[m'*20)
print('\033[31;40mAnalisador de Triâgulos                 \033[m')
print('\033[33m-=\033[m'*20)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[7;30mOs segmentos acima PODEM FORMAR UM TRIÂGULO!\033[m')
else:
    print('\033[7;30mOs segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!\033[m')