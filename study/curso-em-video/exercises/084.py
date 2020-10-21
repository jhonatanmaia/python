pessoas=[]
dados=[]
contador=0
# Em vez de ter um contador, pode usar um len(lista) e ira descobrir a mesma coisa
mais_pesado = menos_pesado = 0.0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    if contador == 0:
        mais_pesado+=dados[1]
        menos_pesado+=dados[1]
    else:
        if dados[1]>mais_pesado:
            mais_pesado=0
            mais_pesado+=dados[1]
        elif dados[1]<menos_pesado:
            menos_pesado=0
            menos_pesado+=dados[1]
    pessoas.append(dados[:])
    dados.clear()
    contador+=1
    sair=str(input('Deseja sair? [S/N] ')).strip().upper()
    while sair != 'S' and sair != 'N':
        sair=str(input('Deseja sair? [S/N] ')).strip().upper()
    if sair == 'S':
        break
pesados=[]
leves=[]
print(f'Foram cadastradas {contador} pessoas.')
for p in pessoas:
    if p[1] == mais_pesado:
        pesados.append(p)
    elif p[1] == menos_pesado:
        leves.append(p)
print(f'O maior peso foi de {mais_pesado}Kg. Peso de',end='')
for p in pesados:
    print(f' {p[0]}',end='')
print()
print(f'O menor peso foi de {menos_pesado}Kg. Peso de',end='')
for p in leves:
    print(f' {p[0]}',end='')