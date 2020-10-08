import math

n2=int(input('Digitte um numero: '))
print('O dobro de {} é {}, o triplo é {} e a raiz é {}'.format(n2,n2*2,n2*3,n2**(1/2)))
print('O dobro de {} é {}, o triplo é {} e a raiz é {:.2f}'.format(n2,n2*2,n2*3,math.sqrt(n2)))