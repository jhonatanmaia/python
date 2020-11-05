def formatacao(valor=0,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')


def aumentar(valor=0,acrescimo=0,formatar=False):
    total=valor*(1+(acrescimo/100))
    return total if formatar is False else formatacao(total)
    

def diminuir(valor=0,decrescimo=0,formatar=False):
    total=valor*(1-(decrescimo/100))
    return total if formatar is False else formatacao(total)

    
def dobro(valor=0,formatar=False):
    total=valor*2
    return total if formatar is False else formatacao(total)

    
def metade(valor=0,formatar=False):
    total=valor/2
    return total if formatar is False else formatacao(total)
    
    
def resumo(p=0,acrescimo=0,decrescimo=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{formatacao(p)}')
    print(f'Dobro do preço: \t{dobro(p,True)}')
    print(f'Metade do preço: \t{metade(p,True)}')
    print(f'{acrescimo}% de aumento: \t{aumentar(p,acrescimo,True)}')
    print(f'{decrescimo}% de redução: \t{diminuir(p,decrescimo,True)}')
    print('-'*30)
    
