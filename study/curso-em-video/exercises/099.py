def maior(* num):
    print('-='*30)
    print('Analisando os valroes passados...')
    maior_numero=max(num[0])
    tamanho=len(num[0])
    for i in num[0]:
        print(f'{i} ',end='')
    print(f'Foram informados {tamanho} valores ao todo.')
    print(f'O maior valor informado foi {maior_numero}')
    print('-='*30)


lista=[]

while True:    
    lista.append(int(input('Digite um valor: ')))
    sair=str(input('Deseja sair? [S/N] ')).upper()
    while sair != 'S' and sair != 'N':
        sair=str(input('Erro, digite novamente [S/N] ')).upper()
    if sair == 'S':
        break
    
maior(lista)