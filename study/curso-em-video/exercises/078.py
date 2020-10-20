'''
lista=[]
for i in range(0,5):
    lista.append(int(input(f'Digite um número no indice {i}: ')))
maior_checagem=max(lista)
checar=lista.count(maior_checagem)    
if checar>1:
    posicao=lista.index(maior_checagem)
    segunda_posicao=lista.index(maior_checagem,posicao+1)
    print(f'O maior valor foi {max(lista)} nos indices {posicao} e {segunda_posicao}')
elif checar == 1:
    print(f'O maior valor foi {max(lista)} no indice {lista.index(max(lista))}')
menor_checagem=min(lista)
checar2=lista.count(menor_checagem)
if checar2>1:
    posicao2=lista.index(menor_checagem)
    segunda_posicao_2=lista.index(menor_checagem,posicao2+1)
    print(f'O menor valor foi {min(lista)} nos indices {posicao2} e {segunda_posicao_2}')
elif checar2 == 1:
    print(f'O menor valor foi {min(lista)} no indice {lista.index(max(lista))}')
'''
lista_um=[]
menor = maior = 0;
for c in range(0,5):
    lista_um.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c== 0:
        maior = menor = lista_um[c]
    else:
        if lista_um[c] > maior:
            maior = lista_um[c]
        elif lista_um[c] < menor:
            menor = lista_um[c]
print('-'*50)
print(f'Você digitou os valores {lista_um}')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(lista_um):
    if v==maior:
        print(f'{i} ',end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(lista_um):
    if v==menor:
        print(f'{i} ',end='')
print()