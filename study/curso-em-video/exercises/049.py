x=int(input('Digite o n�mero da tabuada: '))

print('-'*20)

for a in range(1,11):
    print('{} x {} = {}'.format(a,x,a*x))