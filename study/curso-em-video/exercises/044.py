produto=float(input('Digite o valor do produto: '))
print('Pagamento')
pagamento=int(input('1 - Dinheiro 2 - Cartão'))
if pagamento == 1:
    print('O valor a ser pago é: R$ {:.2f}'.format(produto*0.9))
elif pagamento == 2:
    escohla_pagamento=int(input('1 - A vista 2 - Parcelado'))
    if escohla_pagamento==1:
        print('O valor a ser pago é: R$ {:.2f}'.format(produto*0.95))
    elif escohla_pagamento==2:
        parcelamento=int(input('Quantas vezes será pago?'))
        if parcelamento == 2:
            print('O valor a ser pago é 2x de : R$ {:.2f}'.format(produto/2))
        elif parcelamento >2:
            print('O valro a ser pago é {}x de : R$ {:.2f}'.format(parcelamento,produto*1.2/parcelamento))