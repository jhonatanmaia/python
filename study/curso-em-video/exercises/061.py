primeiro_termo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao da PA:'))
contagem=1
while contagem<11:
    print('PA: {}'.format(primeiro_termo))
    primeiro_termo+=razao
    contagem+=1