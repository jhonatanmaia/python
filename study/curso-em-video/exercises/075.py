x=(int(input('Digite um valor: ')),int(input('Digite um valor: ')),
   int(input('Digite um valor: ')),int(input('Digite um valor: ')))
print(f'O valor 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'O valor 3 aparece primeiro no índice {x.index(3)}')
else:
    print('O número 3 não foi digitado')
print('Os valores pares foram: ', end='')
for i in x:
    if i%2==0:
       print(i,end=' ')