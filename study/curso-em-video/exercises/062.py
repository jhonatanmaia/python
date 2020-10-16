primeiro_termo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao da PA:'))
contagem=1
while contagem<11:
    print('-> {}'.format(primeiro_termo), end='')
    primeiro_termo+=razao
    contagem+=1
    if contagem == 11:
        subtracao=int(input('Você deseja ver mais quantos termos?: '))
        if subtracao != 0:
            contagem-=subtracao
            