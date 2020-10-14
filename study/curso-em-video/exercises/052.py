'''
x=int(input('Digite um numero: '))

if x%2!=0 and x%3!=0 and x%4!=0 and x%5!=0 and x%6!=0 and x%7!=0 and x%8!=0 and x%9!=0:
    print('{} é um numero primo'.format(x))
elif x==2 or x==3 or x==5 or x==7:
    print('{} é um numero primo'.format(x))
else:
    print('{} não é um numero primo'.format(x))
'''
num=int(input('Digite um numero: '))
tot=0
for c in range(1,num+1):
    if num% c==0:
        tot+=1
if tot==2:
    print('O numero e primo')
else:
    print('O numero nao e primo')