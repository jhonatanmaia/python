from datetime import date
atual=date.today().year
maior=0
menor=0
for i in range(0,7):
    x=int(input('Digite o ano de nascimento: '))
    if atual-x>18:
        maior+=1
    else:
        menor+=1
print('Há {} maiores de idade'.format(maior))
print('Há {} menores de idade'.format(menor))