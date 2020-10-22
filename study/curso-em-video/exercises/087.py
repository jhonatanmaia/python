matriz=[]
dados=[]
x=y=pares=terceira_coluna=0
for i in range(0,9):
    dados.append(int(input(f'Digite um valor para [{y}, {x}]: ')))
    if dados[0]%2==0:
        pares+=dados[0]
    if x == 2:
        terceira_coluna+=dados[0]
    matriz.append(dados[:])
    dados.clear()
    x+=1
    if x == 3:
        x=0
        y+=1
x=0
print('-='*20)
for j in matriz:
    print(f'[ {j[0]} ]',end='')
    x+=1
    if x==3 or x==6 or x==9:
        print()
print('-='*20)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira_coluna}')
print(f'O maior valor da segudna linha é {max(matriz[3], matriz[4], matriz[5])}')