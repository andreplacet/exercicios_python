contagem = ('zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez')
while True:
    n = int(input('VALOR INVALIDO! Digite novamente um número entre 0 e 10: '))
    if 0 <= n <= 10:
        break
print(f'voce digitou o número {contagem[n]}')
