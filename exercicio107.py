import modulo_moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é: {modulo_moeda.metade(p)}')
print(f'O dobro de {p} é: {modulo_moeda.dobro(p)}')
print(f'Aumentando {p} em 10% temos: {modulo_moeda.aumentar(p)}')
print(f'Diminuindo {p} em 13% temos: {modulo_moeda.diminuir(p)}')
