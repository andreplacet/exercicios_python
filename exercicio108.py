import modulo_moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$: {modulo_moeda.moeda(p)} é: R$: {modulo_moeda.moeda(modulo_moeda.metade(p))}')
print(f'O dobro de R$: {modulo_moeda.moeda(p)} é: R$: {modulo_moeda.moeda(modulo_moeda.dobro(p))}')
print(f'Aumentando R$: {modulo_moeda.moeda(p)} em 10% temos: R$: {modulo_moeda.moeda(modulo_moeda.aumentar(p))}')
print(f'Diminuindo R$: {modulo_moeda.moeda(p)} em 13% temos: R$: {modulo_moeda.moeda(modulo_moeda.diminuir(p))}')
