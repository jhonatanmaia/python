nome=input('Digite seu nome completo: ')
lista=nome.split()
lista2=lista[::-1]
print('{} {}'.format(lista[0],lista2[0]))
print('{} {}'.format(lista[0],lista[len(lista)-1]))