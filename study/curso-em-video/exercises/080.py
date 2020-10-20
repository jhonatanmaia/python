'''
lista=[]
for i in range(0,5):
    numero=int(input('Digite um numero: '))
    if len(lista) == 0:
        lista.append(numero)
        print('Adicionado o primeiro valor.')
    elif len(lista) == 1:
        if numero>lista[0]:
            lista.insert(1,numero)
            print('Adicionado ao fim da lista.')
        elif numero<lista[0]:
            lista.insert(0,numero)
            print('Adicionado ao inicio da lista.')
        else:
            lista.append(numero)
            print('Adicionado a lsita.')
    elif len(lista) == 2:
        if lista[0]<numero<lista[1]:
            lista.insert(1,numero)
            print('Adicionado ao indice 1.')
        elif numero>lista[1]:
            lista.insert(2,numero)
            print('Adicionado ao indice 2.')
        else:
            lista.insert(0,numero)
            print('Adicionado ao indice 0.')
    elif len(lista) == 3:
        if lista[0]<numero<lista[1]:
            lista.insert(1,numero)
            print('Adicionado ao indice 1.')
        elif lista[1]<numero<lista[2]:
            lista.insert(2,numero)
            print('Adicionado ao indice 2.')
        elif numero>lista[2]:
            lista.insert(3,numero)
            print('Adicionado ao indice 3.')
        else:
            lista.insert(0,numero)
            print('Adicionado ao indice 0.')
    elif len(lista) == 4:
        if lista[0]<numero<lista[1]:
            lista.insert(1,numero)
            print('Adicionado ao indice 1.')
        elif lista[1]<numero<lista[2]:
            lista.insert(2,numero)
            print('Adicionado ao indice 2.')
        elif lista[2]<numero<lista[3]:
            lista.insert(3,numero)
            print('Adicionado ao indice 3.')
        elif numero>lista[3]:
            lista.insert(4,numero)
            print('Adicionado ao indice 4.')
        else:
            lista.insert(0,numero)
            print('Adicionado ao indice 0')
print(f'Os valores digitados em forma crescente foram: {lista}')
'''

lista = []
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c == 0 or n>lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lsita')
    else:
        pos=0
        while pos<len(lista):
            if n<= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos}')
                break
print(f'A lista digitada foi {lista}')