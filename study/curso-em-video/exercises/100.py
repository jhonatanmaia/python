import time
import random

def sorteio(lista):
    for i in range(0,5):
        lista.append(random.randint(1,10))
        # Poderia ter posto o print dos numeros aqui dentro
    print('Sortenando 5 valores da lsita: ',end='')
    for i in lista:
        time.sleep(0.25)
        print(f'{i} ',end='')
    print('PRONTO!')
    
    
def somaPar(lista):
    time.sleep(0.5)
    soma=0
    for i in lista:
        if i%2==0:
            soma+=i
    print(f'Somando os valroes pares de {lista}, temos {soma}')
    
    
numeros=[]
sorteio(numeros)
somaPar(numeros)