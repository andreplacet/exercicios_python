import modulo_moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$: {modulo_moeda.moeda(p)} é: R$: {modulo_moeda.metade(p, show=True)}')
print(f'O dobro de R$: {modulo_moeda.moeda(p)} é: R$: {modulo_moeda.dobro(p, show=True)}')
print(f'Aumentando R$: {modulo_moeda.moeda(p)} em 10% temos: R$: {modulo_moeda.aumentar(p, show=True)}')
print(f'Diminuindo R$: {modulo_moeda.moeda(p)} em 13% temos: R$: {modulo_moeda.diminuir(p, show=True)}')
