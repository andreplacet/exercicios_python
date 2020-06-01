nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Calculando {:.1f} e {:.1f}, a média do aluno foi {:.1f}'.format(nota1, nota2, media))
if media >=5 and media < 7:
    print('O aluno esta de recuperação, com média {:.1f}'.format(media))
elif media < 5:
    print('O aluno esta reprovado! com média {}'.format(media))
elif media >= 7:
    print('O aluno esta aprovado! com média {}'.format(media))