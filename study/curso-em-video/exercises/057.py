sexo=''
sexo=str(input('Digite seu sexo [F/M]: ')).upper()[0]
while sexo!='M' and sexo!='F':
    sexo=str(input('Sexo inválido, digite seu sexo [F/M]: ')).upper()
print('Sexo {} registrado com sucesso.'.format(sexo))