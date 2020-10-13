soma=0
for i in range(0,6):
    x=int(input('Digite um numero inteiro: '))
    if x%2==0:
        soma+=x
print('A soma de todos os numeros pares é {}'.format(soma))