def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    if show==False:
        num=1
        for i in range(n,0,-1):
            num*=i
        return num
    elif show==True:
        num=1
        for i in range(n,0,-1):
            num*=i
            if i>1:
                print(f'{i} x ',end='')
            else:
                print(f'{i} = ',end='')
        return num
    

print(fatorial(10,True))