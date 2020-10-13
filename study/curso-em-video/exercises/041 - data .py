from datetime import date
atual = date.today().year
a2=int(input('Digite seu ano de nascimento: '))
a1=atual-a2
if a1<=9:
    print('Mirim')
elif a1<=14:
    print('Infantil')
elif a1<=19:
    print('Junior')
elif a1==20:
    print('Senior')
elif a1>20:
    print('Master')