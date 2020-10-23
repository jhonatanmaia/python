jogador={}
gols_marcados=[]
soma=gols=0
jogador['nome']=str(input('Nome do Jogador: '))
partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0,partidas):
    gols=int(input(f'Quantos gols na partida {i}? '))
    soma+=gols
    gols_marcados.append(gols)
    # poderia usado a função sum() para somar a lista de gols
jogador['gols']=gols_marcados
jogador['total']=soma
print('-='*30)
print(jogador)
print('-='*30)
for chave,valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for indice,valor in enumerate(gols_marcados):
    print(f'    => Na partida {indice}, fez {valor} gols.')
print(f'Foi um total de {soma} gols.')