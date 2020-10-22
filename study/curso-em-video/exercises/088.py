import random
import time
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
jogo=[]
quantidade=int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=   SORTEANDO {quantidade} JOGOS -=-=-=')
for i in range(0,quantidade):
    jogo.append(random.sample(range(1,60),6))
    jogo[i].sort()
for indice,valor in enumerate(jogo):
    time.sleep(0.5)
    print(f'Jogo {indice+1}: {valor}')