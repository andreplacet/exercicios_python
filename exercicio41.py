from datetime import date
nascimento = int(input('Qual seu ano de nascimento!'))
anoatual = date.today().year
resultado = anoatual - nascimento
if resultado <= 9:
    print('Este atleta de classifica na categoria MIRIM! e tem {} anos.'.format(resultado))
elif resultado > 9 and resultado < 14:
    print('Este atleta se classifica na categoria INFANTIL! e tem {} anos.'.format(resultado))
elif resultado >=14 and resultado < 19:
    print('Este atleta se classifica na categoria JUNIOR! e tem {} anos.'.format(resultado))
elif resultado >= 19 and resultado < 25:
    print('Este atleta se classifica na categoria SÊNIOR! e tem {} anos'.format(resultado))
elif resultado >= 25:
    print('Este atleta se classifica na categoria MASTER! e tem {} anos'.format(resultado))
