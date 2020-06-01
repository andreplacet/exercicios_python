print('{:=^40}'.format('Lojas Andre Luiz'))
preco = float(input('Valor da Compra: R$:'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Selecione a opção: '))
if opcao == 1:
    resultado = preco - (preco * 0.10)
    print('Sua compra tem o total de {:.2f}, pagamento a vista em dinheiro com 10% de desconto {:.2f}!'.format(preco, resultado))
elif opcao == 2:
    resultado = preco - (preco * 0.05)
    print('Sua compra  tem o total de {:.2f}, pagamento a vista no cartão com 5% de desconto {:.2f}'.format(preco, resultado))
elif opcao == 3:
    resultado = preco / 2
    print('Sua compra no valor de {:.2f} em duas parcelas sem juros de {:.2f}'.format(preco, resultado))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas? '))
    resultado = preco + (preco * 0.20)
    parcelamento = resultado / parcelas
    print('Sua compra no valor de {:.2f}, parcelada em {}x, com juros de 20% será de 4 parcelas de {:.2f}, no valor total de {:.2f}'.format(preco, parcelas, parcelamento, resultado))
else:
    print('Opção invalida de Pagamento! Tente Novamente!')