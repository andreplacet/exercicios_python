soma = homens = mulheres = pessoas18 = pessoasmenor18 = 0
while True:
    print('-'*15)
    print('CADASTRE UMA PESSOA')
    print('-'*15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper()
    if idade > 18:
        pessoas18 += 1
    else:
        pessoasmenor18 += 1
    while sexo not in 'MF':
        print('\033[31mSEXO INVALIDO, TENTE NOVAMENTE!\033[m')
        sexo = str(input('Sexo: ')).upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('-'*15)
    resp = str(input('Quer continuar?  [S/N]')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).upper().strip()
    if resp in 'N':
        break
print('='*10, 'FIM DO PROGRAMA', '='*10)
print(f'Total de pessoas com mais de 18 anos: {pessoas18}')
print(f'Total de pessoas com menos de 18 anos: {pessoasmenor18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulher(es) com menos de 20 anos')
