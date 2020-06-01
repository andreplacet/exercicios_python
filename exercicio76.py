listagem = ('Lapis', 0.95, 'Borracha', 0.50, 'Tesoura', 3.90, 'Estojo', 4.95, 'Caneta Preta', 1.10,
            'Caneta vermelha', 1.10, 'Caderno', 15.90, 'Mochila Xtreme', 59.90)
print('-'*34)
print(f'{"LISTA ESCOLAR":^34}')
print('-'*34)
for posicao in range(0, len(listagem), 2):
    print(f'{listagem[posicao]:.<30}{listagem[posicao+1]:.2f}')