'''

Usado quando não sabemos a quantidade de passos

enquanto não algo
    passo
pega

while nao algo
    passo
pega

https://note.nkmk.me/en/python-multi-variables-values/

'''

for i in range(1,10):
    print(i)
print('Fim')

j=1
while j<10:
    print(j)
    j+=1
print('Fim')

a='S'
while a=='S':
    a1=int(input('Digite um valor: '))
    a=str(input('Deseja continuar? [S/N]')).upper()
print('Fim')

b = 1
par = impar = 0
while b!=0:
    b=int(input('Digite um numero: '))
    if b%2==0:
        par=+1
    else:
        impar=+1
print('Numeros pares digitado: {} - Numeros impares digitados: {}'.format(par,impar))