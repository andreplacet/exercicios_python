nome = str(input('Qual seu nome? ')).strip()
altura = float(input('Qual Sua Altura? (m)'))
peso = float(input('Qual o seu peso? (kg)'))
imc = peso / (altura ** 2)
print('O seu imc {}, é de {:.1f}!'.format(nome.capitalize(), imc))
if imc < 18.5:
    print('Voce esta abaixo do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Voce esta no seu peso ideal')
elif 25 <= imc < 30:
    print('Voce esta no sobrepeso')
