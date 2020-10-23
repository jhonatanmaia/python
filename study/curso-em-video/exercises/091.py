import random
import time
from operator import itemgetter
jogadores={'Jogador 1':random.randint(1,6),'Jogador 2':random.randint(1,6),
           'Jogador 3':random.randint(1,6),'Jogador 4':random.randint(1,6)}
for chave,valor in jogadores.items():
    time.sleep(0.5)
    print(f'O {chave} tirou {valor}')
print('-='*30)
sort=sorted(jogadores.items(),key=lambda x:x[1],reverse=True)
# Outra forma de sortear
raking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1),reverse=True)
print('Ranking dos Jogadores!')
posicao=1
for i in sort:
    time.sleep(0.5)
    print(f'{posicao}º lugar: {i[0]} com {i[1]}')
    posicao+=1
print('-'*40)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(0.5)