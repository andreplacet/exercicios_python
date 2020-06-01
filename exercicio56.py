aux = 0
somafeminino = 0
media = 0
nomemaior = ''
idademaior = 0
for p in range(1, 5):
    print(' ---- {}ª PESSOA ---- '.format(p))
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]')).upper().strip()
    aux += idade
    media = aux / p
    if p == 1 and sexo == 'M':
        idademaior = idade
        nomemaior = nome
    if sexo == 'M' and idade > idademaior:
        idademaior = idade
        nomemaior = nome
    if sexo == 'F' and idade < 20:
        somafeminino += 1
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homen mais velho tem {} anos, e se chama {}.'.format(idademaior, nomemaior))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(somafeminino))
