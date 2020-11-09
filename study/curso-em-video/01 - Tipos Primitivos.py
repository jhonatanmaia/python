'''
=  -> recebe
== -> iguala

int -> numero inteiro
float -> numero quebrado, ponto flutuante
bool -> true e false
str -> texto


n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s=n1+n2
print('A soma vale {}'.format(s))
print('A soma entre {} e {} vale {}'.format(n1,n2,s))

#isnumerico diz se e possivel converter um valor para numerico
n=input('Digite algo: ')
print(n.isnumeric())
#isalpha diz se e letra
print(n.isalpha())
#isalnum diz se e alfa numerico
print(n.isalnum())
'''