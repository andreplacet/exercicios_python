soma = maisdemil = contador = precomenor = 0
nomemenor = ''
print('===== \033[7;30mLOJA DO RUBÃO\033[m ====')
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    soma += preco
    contador += 1
    if contador == 1:
        nomemenor = produto
        precomenor = preco
    if preco < precomenor:
        nomemenor = produto
        precomenor = preco
    if preco > 1000:
        maisdemil += 1
    resp = str(input('Continuar comprando? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Continuar comprando? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('\033[33m-\033[m'*37)
print('====== CARRINHO ======')
print(f'valor total da compra R$:\033[33m{soma:.2f}\033[mreais')
print(f'{maisdemil} produtos custam mais de R$:\033[33m1000,00\033[mreais')
print(f'"{(nomemenor).capitalize()}" foi o produto mais barato e custou R$:\033[33m{precomenor:.2f}\033[mreais')
print('\033[33m-\033[m'*37)
