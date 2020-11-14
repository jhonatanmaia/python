'''
break - para o loop

# Um loop infinito
while True:
    print(cont)
    cont+=1
    
'''
cont=1
while cont<=10:
    print(cont)
    cont+=1

n = cont2 = s = 0
while True:
    n=int(input('Digite um número: '))
    cont2+=1
    if n == 999:
        break
    s+=n
#print('A soma é {}'.format(s))
print(f'A soma vale {s}')