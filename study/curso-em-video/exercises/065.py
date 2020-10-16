menu=''
media=0
soma=0
maior=0
menor=0
while menu!='N':
    numeros=int(input('Digite um numero: '))
    soma+=numeros
    menu=str(input('Deseja continuar? [S/N]: ')).upper()
    media+=1
    menor=numeros
    if media == 1:
        maior = menor = numeros
    else: 
        if numeros>maior:
            maior=numeros
        if numeros<menor:
            menor=numeros
print('A media foi {}'.format(soma/media))
print('O maior foi {}'.format(maior))
print('O menor foi {}'.format(menor))