x=int(input('Digite o número da tabuada: '))

print('-'*20)

for a in range(1,11):
    print('{} x {} = {}'.format(a,x,a*x))