numero=input('Digite um numero entre 0 a 9999: ')
print('{} Unidade \n{} Dezenas\n{} Centenas\n{} Milhar'.format(numero[0],numero[1],numero[2],numero[3]))

numero2=int(input('Digite um numero: '))
texto=[int(numero2) for numero2 in str(numero2)]
print('{} Unidade \n{} Dezenas\n{} Centenas\n{} Milhar'.format(texto[0],texto[1],texto[2],texto[3]))

u = numero2 // 1 % 10
d = numero2 // 10 % 10
c = numero2 // 100 % 10
m = numero2 // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))