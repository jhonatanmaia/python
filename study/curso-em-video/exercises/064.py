print('Digite os numeros para serem somados ou digite 999 para sair')
cont=0
numeros=0
soma=0
numeros=int(input('Digite um numero: '))
while numeros!=999:
    numeros=int(input('Digite um numero: '))
    soma+=numeros
    cont+=1
print('A soma é {} e a quantidade de numeros digitados foram {}'.format(soma-999,cont-1))