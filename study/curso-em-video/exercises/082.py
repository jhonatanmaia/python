lista=[]
impares=[]
pares=[]

while True:
    lista.append(int(input('Digite um numero: ')))
    saida=str(input('Voce deseja sair? [S/N] ')).strip().upper()
    while saida != 'S' and saida != 'N':
        saida=str(input('Erro, digite novamente. Deseja sair? [S/N] ')).strip().upper()
    if saida=='S':
        break

for indice,valor in enumerate(lista):
    if valor%2==0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Lista normal: {lista}')
print(f'Lista pares: {pares}')
print(f'Lista impares: {impares}')