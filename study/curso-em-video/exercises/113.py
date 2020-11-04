def leiaInt(num=''):
    while True:
        try:
            a=int(num)
        except ValueError:
            num=str(input('Digite um número inteiro válido: '))
        except KeyboardInterrupt:
            print('Usuario parou o programa. ')
        else:
            return a
            break
    

#=leiaInt(str(input('Digite um número inteiro: ')))
#print(a)

def leiaFloat(num=''):
    while True:
        try:
            a=float(num)
        except ValueError:
            num=str(input('Digite um número flutuante válido: '))
        except KeyboardInterrupt:
            print('Usuario parou o programa.')
        else:
            return a
            break


a=leiaFloat(str(input('Digite um numero: ')))
print(a)