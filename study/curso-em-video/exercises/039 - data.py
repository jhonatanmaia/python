from datetime import date
atual = date.today().year
nasc=int(input('Ano nascimento'))
idade=atual-nasc
if idade==18:
    print('Va se alistar')
elif idade<18:
    print('Voce aidna nao tem 18 anos, faltam {} anos'.format(18-idade))
else:
    print('VOce ja se alsitou')
