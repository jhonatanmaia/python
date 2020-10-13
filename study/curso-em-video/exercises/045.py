import random
maquina=random.randint(1,3)

jogador=int(input('1 - Pedra 2 - Papel 3- Tesoura:'))
if jogador==maquina:
    print('Empate')
elif jogador == 1 and maquina == 3:
    print('Você ganhou!')
elif jogador == 2 and maquina == 1:
    print('Você ganhou!')
elif jogador == 3 and maquina == 2:
    print('Você ganhou!')
else:
    print('Você perdeu!')