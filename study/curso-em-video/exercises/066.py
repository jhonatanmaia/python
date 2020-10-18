print('-'*40)
print('Digite 999 para sair.')
print('-'*40)
contador=soma=0
while True:
    numeros=int(input('Digite um número: '))
    if numeros == 999:
        break
    contador+=1
    soma+=numeros
print(f'Você digitou {contador} números e a soma foi {soma}.')