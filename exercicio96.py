def area(largura, comprimento):
    a = largura * comprimento
    print(f'A aŕea do terreno de medidas {largura:.2f}x{comprimento:.2f} em mts² é: {a:.1f}mt²')


l = float(input('LARGURA (m):'))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
