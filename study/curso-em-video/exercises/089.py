lista=[]
dado_nome=[]
dado_nota=[]
x=0
while True:
    dado_nome.append(str(input('Digite o nome do aluno: ')))
    lista.append(dado_nome[:])
    dado_nome.clear()
    dado_nota.append(float(input('Digite a primeira nota: ')))
    dado_nota.append(float(input('Digite a segunda nota: ')))
    lista[x].append(dado_nota[:])
    dado_nota.clear()
    x+=1
    sair=str(input('Deseja sair? [S/N] ')).strip().upper()
    if sair == 'S':
        break
print('-='*40)
print(f'No. {"NOME":^10} {"MÉDIA":^12}')
print('-'*30)
for i in range(0,x):
    nome=lista[i]
    print(f'{i} {lista[i][0]:^15} {(lista[i][1][0]+lista[i][1][1])/2}')
print('-'*30)
while True:
    notas=int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    print('-'*30)
    print(f'Notas de {lista[notas][0]} são {lista[notas][1]}')