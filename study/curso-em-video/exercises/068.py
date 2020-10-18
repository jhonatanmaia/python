import random
# Jogo para quando voce perder
print('-'*40)
print('Par ou Ímpar - O Jogo')
print('-'*40)
contador_vitorias=0
while True:
    pc=random.randint(0,10)
    numero=int(input('Digite um número: '))
    decisao=str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    soma=pc+numero
    if soma%2 == 0 and  decisao == 'P' or soma%2 != 0 and decisao == 'I':
        print('Você venceu!')
        contador_vitorias+=1
    elif soma%2 == 0 and  decisao == 'I' or soma%2 != 0 and decisao == 'P':
        break
    print('Vamos jogar novamente...')
print(f'Você perdeu e ganho {contador_vitorias} vezes')