operacao=0
valor1=int(input('Digite um valor: '))
valor2=int(input('Digite um valor: '))
while operacao!=5:
    operacao=int(input('''
    Menu
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa
    Opção:'''))
    if operacao == 1:
        print('A soma é: {}'.format(valor1+valor2))
    elif operacao == 2:
        print('A multiplicação é: {}'.format(valor1*valor2))
    elif operacao == 3:
        if valor1>valor2:
            print('O maior número é: {}'.format(valor1))
        else:
            print('O maior número é: {}'.format(valor2))
    elif operacao == 4:
        valor1=int(input('Digite um valor: '))
        valor2=int(input('Digite um valor: '))
    elif operacao == 5:
        break
    else:
        print('Operacao invalidade, tente novamente')
print('Programa Encerrado')