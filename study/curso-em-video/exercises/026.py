frase=str(input('Digite uma frase: ')).strip()
print('Há {} letras a na frase'.format(frase.lower().count('a')))
print('A letra a está na posicao {} pela primeira vez'.format(frase.lower().find('a')+1))
posicaoUltimoA=frase.lower()[::-1].find('a')
print('A ultima vez que a letra a aparece e na posicao {}'.format(len(frase)-posicaoUltimoA))
print('A letra a está na posicao {} pela primeira vez'.format(frase.lower().rfind('a')+1))