def ficha(nome='',gols=0):
    if nome=='':
        print(f'O jogador <desconhecido> fez {gols} gols(s) no campeonato.')
    elif nome=='' and gols == 0:
        print('O jogador <desconhecido> fez 0 gols no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador=str(input('Nome do Jogador: ')).strip()
gols=str(input('Numero de Gols: ') or 0) 
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0

ficha(jogador,gols)   