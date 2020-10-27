def contador():
    import time
    print('-='*15)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1,11):
        print(f'{i} ',end='')
        time.sleep(0.25)
    print('FIM!')
    print('-='*15)
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10,-2,-2):
        print(f'{i} ',end='')
        time.sleep(0.25)
    print('FIM!')
    print('-='*15)
    print('Agora é a sua vez de personalizar a contagem!')
    inicio=int(input('Inicio: '))
    fim=int(input('Fim: '))
    passo=int(input('Passo: '))
    if passo == 0:
        passo=1
    if passo <0 and inicio < fim:
        passo*=(-1)
    print(f'Contadem de {inicio} até {fim} de {passo} em {passo}')
    if inicio>fim and passo < 0:
        for i in range(inicio,fim+passo,passo):
            print(f'{i} ',end='')
            time.sleep(0.25)
    elif inicio>fim and passo > 0:
        for i in range(inicio,fim-passo,passo*(-1)):
            print(f'{i} ',end='')
            time.sleep(0.25)
    else: 
        for i in range(inicio,fim+1,passo):
            print(f'{i} ',end='')
            time.sleep(0.25)
    print('FIM!')


contador()