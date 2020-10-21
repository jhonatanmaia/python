lista=[]
while True:
    numero=int(input('Digite um numero: '))
    lista.append(numero)
    saida=str(input('Deseja sair? [S/N] ')).strip().upper()
    while saida != 'S' and saida != 'N':
        saida=str(input('Erro, digite novamente. Deseja sair? [S/N] ')).strip().upper()
    if saida == 'S':
        break
print(f'Foram digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
print(f'O número 5 apareceu {lista.count(5)} vezes.')