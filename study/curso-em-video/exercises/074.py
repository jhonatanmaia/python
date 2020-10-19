from random import randint
tupla=(randint(0,50),randint(0,50),randint(0,50),randint(0,50),randint(0,50))
print(f'A tupla é {tupla}')
x=sorted(tupla)
print('O maior número é {} e o menor é {}'.format(x[4],x[0]))
print(f'O maior número é {max(tupla)} e o menor é {min(tupla)}')