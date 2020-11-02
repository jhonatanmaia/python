def leiaInt(n):
    j=input(f'{n}')
    while True:
        try:
            int(j)
            float(j)
            return j
            break
        except ValueError:
            j=input('Erro, digite novamente: ')


n=leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')