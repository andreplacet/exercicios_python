lado1 = int(input('Primeiro segmento: '))
lado2 = int(input('Segundo segmento: '))
lado3 = int(input('Terceiro Segmento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 and lado1 == lado3:
        print('Esse triangulo é um triangulo Equilatero!')
        print('\033[7;30mOs segmentos acima PODEM FORMAR UM TRIÂGULO!\033[m')
    elif lado1 == lado2 or lado1 == lado3:
        print('Esse triangulo é um triangulo Isósceles!')
        print('\033[7;30mOs segmentos acima PODEM FORMAR UM TRIÂGULO!\033[m')
    elif lado1 != lado2 != lado3 != lado1:
        print('Esse triangulo é um triangulo Escaleno!')
        print('\033[7;30mOs segmentos acima PODEM FORMAR UM TRIÂGULO!\033[m')
else:
    print('\033[7;30mOs segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!\033[m')

