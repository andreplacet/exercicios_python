dicionario = {}
dicionario['nome'] = str(input('Nome: ').capitalize().strip())
dicionario['media'] = float(input(f'Média de {dicionario["nome"]} '))
if dicionario['media'] >= 7:
    dicionario['situação'] = 'Aprovado'
elif 5 <= dicionario['media'] < 7:
    dicionario['media'] = 'Recuperação'
else:
    dicionario['situação'] = 'Reprovado'
print(f'O aluno {dicionario["nome"]}, teve média {dicionario["media"]} e esta {dicionario["situação"]}')
for k, v in dicionario.items():
    print(f'- {k} = {v}')