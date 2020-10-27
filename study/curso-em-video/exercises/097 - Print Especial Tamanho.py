def escreva(texto):
    print('-'*(len(texto)+4))
    print(f'  {texto}')
    print('-'*(len(texto)+4))


txt=input(str('Digite uma frase: '))
escreva(txt)