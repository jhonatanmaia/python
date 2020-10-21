lista=[[],[]]
for i in range(0,7):
    numero=int(input('Digite um valor: '))
    if numero%2==0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares foram {lista[0]} e os impares foram {lista[1]}')