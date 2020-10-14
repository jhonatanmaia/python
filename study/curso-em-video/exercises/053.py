'''
x=str(input('Digite uma frase: '))

y= [x.replace(" ","")]

print(y[0].reversed)
'''
frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split()
junto = ''.join(palavras)
inverso=junto[::-1]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')