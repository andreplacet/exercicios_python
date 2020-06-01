#from moduloexterno import fatorial, dobro, tripl
import moduloexterno

num = int(input('Digite um número: '))
fat = moduloexterno.fatorial(num)
print(f'O fatorial de {num} é: {fat}')
print(f'O dobro de {num} é {moduloexterno.dobro(num)}')
print(f'O triplo de {num} é {moduloexterno.tripl(num)}')
