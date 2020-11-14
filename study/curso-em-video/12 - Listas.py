'''
LISTAS SÃO MUTAVEIS
'''

print('-'*20)
lista=[1,2,3,4]
print(lista)
print('-'*20)
lista.append(5)
print(lista)
print('-'*20)
# Adicioan o 6 na posição 0
lista.insert(0,6)
print(lista)
print('-'*20)
# Se quiser remover pela posição/indice use o del ou pop
# Se quiser remover um valor especifico use o remove
del lista[3]
lista.pop(3)
# lista.pop() remove o ultimo elemento
# Remove remove apenas uam vez, para remover mais pode usar um loop
lista.remove(6)
print(lista)
print('-'*20)
# Para fazer condição de remoção
if 10 in lista:
    lista.remove(10)
# Cria uma lsita pelo range
# valores=list[range(4,11)]
# Fazer um sort da lsita
lista.append(3)
lista.append(4)
lista.append(6)
lista.append(7)
lista.append(9)
lista.append(8)
lista.append(0)
print(lista)
lista.sort()
print(lista)
print('-'*20)
# Fazer um sort reverso
lista.sort(reverse=True)
print(lista)
print('-'*20)
# Para pegar o tamanho da lsita
print(len(lista))
print('-'*20)
# E possivel mudar o indice para um valor especifico
lista[0] = 100
print(lista)
print('-'*20)
for v in lista:
    print(f'{v}...',end='')
print('')
print('-'*20)
for i,j in enumerate(lista):
    print(f'Na posição {i} enontrei o valor {j}!')
print('Cheguei no final da lista.')
print('-'*20)
#for cont in range(0,5):
    #lista.append(int(input('Digite um valor: ')))
print(lista)
print('-'*20)
# b vai espelhar a, o que for alterado em b sera alterado em a
a = [2,3,4,7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# para fazer uma copia use
c = [1,3,5,7]
d = c[:]
print(d)
d[2]=9
print(d)
print(c)
print('-'*20)
# Adicionar lista dentro de lsita
# Se não usar o [:] não será gerado um copia mas sim uma substituição
x=[1,2]
y=[]
y.append(x[:])
print(y)
z=[3,4]
y.append(z[:])
print(y)
nomes=[['Paulo',25],['Maria',19],['João',32]]
print(nomes[0][0])
print(nomes[1][1])
print(nomes[2][0])
print(nomes[1])

galera=[]
dados=[]
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')