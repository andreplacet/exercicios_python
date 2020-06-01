from datetime import date
dicionario = dict()
dicionario['nome'] = str(input('Nome: ').capitalize().strip())
ano_nascimento = int(input('Anos de Nascimento: '))
dicionario['idade'] = date.today().year - ano_nascimento
dicionario['ctps'] = int(input('Cartei de Trabalho (0 se não tiver): '))
if dicionario['ctps'] != 0:
    dicionario['contrataçao'] = int(input('Ano de Contratação: '))
    if dicionario['contrataçao'] == date.today().year:
        dicionario['aposentadoria'] = dicionario['idade'] + 60
    else:
        dicionario['salario'] = float(input('Salário: '))
        tempo_trabalhado = (date.today().year - dicionario['contrataçao'])
        dicionario['aposentadoria'] = (dicionario['idade'] + 60) - tempo_trabalhado
else:
    dicionario['ctps'] = 'Não possui'
print('-=' * 30)
for k, v in dicionario.items():
    print(f'{k} = {v}')
lista = dicionario.copy()
print(lista)