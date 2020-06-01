lista = list()
expression = str(input('Digite sua expressão: '))
for letras in expression:
    if letras == '(':
        lista.append(letras)
    if letras == ')':
        lista.pop()
if '(' in lista:
    print('Sua expressão não é valida')
else:
    print('Sua expressão é valida!')