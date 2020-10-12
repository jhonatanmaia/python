from random import randint
# Gerar numeros inteiros
from time import sleep
#poe o computador para dormir por segundos

x=randint(0, 5)
print('---//---'*9)
print('I am thinking in a number between 0 and 5...')
print('---//---'*9)

y=int(input('Enter the number I am thinking: '))

print('LOADING...')
sleep(2)

if x==y:
    print('You are correct!')
else:
    print('You are wrong!')