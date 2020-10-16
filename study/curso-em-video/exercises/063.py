sequencia=int(input('Digite o tamanho da sequencia: '))
contador=0
fibo1,fibo2 = 0,1
while contador < sequencia:
    if sequencia==1 or sequencia == 2:
        print('Sequencia: {}'.format(1))
    print('Sequencia: {}'.format(fibo1))
    fibo3=fibo1+fibo2
    fibo1=fibo2
    fibo2=fibo3
    contador+=1

'''
n = int(input('Quantos termos voce quer mostrar?'))
t1=0
t2=1
print('{} - {}'.format(t1,t2), end='')
cont=3
while cont<=n
    t3=t1+t2
    print('- {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
'''