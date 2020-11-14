'''
Variavel Composta: Tupla
OS itens são acessados pelos indices, começado pelo 0

Tuplas são imutáveis

'''
tupla=(0,1,2,3)
tuplaNova=0,1,2,3
print('---'*20)
# Pegue o indice indicado
print(tupla[2])
print('---'*20)
# Comece no indice x e va ate o indice y
print(tupla[0:2])
print('---'*20)
# Comece no indice x e va ate o final
print(tupla[1:])
print('---'*20)
# Pegue o ultimo elemento
print(tupla[-1])
print('---'*20)
# Mostra o tamanho da tupla
print(len(tupla))
print('---'*20)
# Mostrar tudo com loop
for c in tupla:
    print(c)
print('---'*20)
# Este pode mostrar a posição
for d in range(0, len(tupla)):
    print(tupla[d])
    print(d)
print('---'*20)
for pos,e in enumerate(tupla):
    print(tupla[e])
    print(f'Posição: {pos}')
print('---'*20)
# Outro 01
print(tupla[-3:])
print('---'*20)
# Mostrar organizado
print(sorted(tupla))
print('---'*20)
# Soma de Tuplas
a = (1,3,5)
b = (2,4,6)
c = a + b
print(c)
print(sorted(c))
print('---'*20)
# Contar quantas vezes um objeto especifico
print(c.count(4))
print('---'*20)
# Dizer um indice de um valor especifico
print(c.index(5))
print('---'*20)
# Dizer um indice de um valro especifico começando por um indice x
print(c.index(5,2))
print('---'*20)
# Apaga uma tupla
del(c)
