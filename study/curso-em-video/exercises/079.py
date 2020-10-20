lista=[]
while True:
    valor=int(input('Digite um numero: '))
    if lista.count(valor) == 0:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não será adicionado.')
    saida=str(input('Você deseja sair? [S/N]? ')).strip().upper()
    while saida != 'S' and saida != 'N':
        saida=str(input('Erro, digite novamente [S/N]: '))
    if saida == 'S':
        lista.sort()
        print('-=-'*20)
        print(f'Você digitou os valores {lista}')
        break