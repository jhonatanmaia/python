import math
fatorial=int(input('Digite um numero: '))
resultado=1
while fatorial !=0:
    resultado*=fatorial
    fatorial-=1
print('O resultado do fatorial é: {}'.format(resultado))

resultado2=1
for i in range(fatorial,0,-1):
    resultado2*=i
print('O resultado do fatorial é: {}'.format(resultado2))

print('O resultado do fatorial é: {}'.format(math.factorial(fatorial)))