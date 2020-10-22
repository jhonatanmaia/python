matriz=[]
dados=[]
x = y = 0
# em vez de x e y, poderia ter usado um laço dentro do outro
for i in range(0,9):
    dados.append(int(input(f'Digite um valor para [{y}, {x}]: ')))
    matriz.append(dados[:])
    dados.clear()
    x+=1
    if x == 3:
        x=0
        y+=1
x=0
for j in matriz:
    print(f'[{j[0]:^5}]',end='')
    x+=1
    if x == 3 or x == 6 or x == 9:
        print()