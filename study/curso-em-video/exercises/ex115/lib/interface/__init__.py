def leiaInt(num=''):
    while True:
        try:
            a=int(input(num))
        except (ValueError,TypeError):
            print('Numero invalido.')
            continue
        except KeyboardInterrupt:
            print('Usuario parou o programa. ')
            return 0
        else:
            return a
            break
        

def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opc=leiaInt('Sua Opção: ')
    return opc