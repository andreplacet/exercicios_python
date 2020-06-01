jogador = dict()
gols = list()
jogadores = list()
while True:
    print('-' * 35)
    jogador['nome'] = str(input('Nome do Jogador: ').capitalize().strip())
    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partida):
        gols.append((int(input(f'Quantos gols na partida {c + 1}? '))))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    continuar = str(input('Deseja continuar? [s/n] ').lower()[0])
    while continuar not in 'sn':
        print('VALOR INVALIDO, DIGITE SIM OU NAO PARA CONTINUAR')
        continuar = str(input('Deseja continuar? [s/n] ').lower()[0])
    if continuar == 'n':
        break
print('-' * 35)
print(f'{"COD":<5}{"Nome":<15}{"Gols":<8}{"Total":<8}')
print('-' * 35)
for c in range(0, len(jogadores)):
    print(f'{c:>3}  {jogadores[c]["nome"]:<12}{jogadores[c]["gols"]}{jogadores[c]["total"]:>8}')
print('-' * 35)
while True:
    escolha = int(input('Mostrar dados de qual jogador? (Digite 999 para sair): '))
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print(f'ERRO, NÃO EXISTE JOGADOR COM O CODIGO {escolha}!!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["nome"]}')
        for i, g in enumerate(jogadores[escolha]['gols']):
            print(f'No jogo {i + 1} fez {g} gols')
print('PROGRAMA FINALIZADO')