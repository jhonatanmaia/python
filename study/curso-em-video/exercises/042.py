a1=float(input('Digite o lado 1: '))
a2=float(input('Digite o lado 2: '))
a3=float(input('Digite o lado 3: '))

condicao_verdadeira= a1+a2>a3 and a1+a3>a2 and a2+a3>a1

triangulo_equilatero= a1==a2==a3
triangulo_isoceles= a1==a2 or a1==a3 or a2==a3
triangulo_escaleno= a1!=a2 and a1!=a3 and a2!=a3

if condicao_verdadeira == True:
    print('Pode ser formado um triangulo')
    if triangulo_equilatero ==True:
        print('Triangulo equilatero')
    elif triangulo_isoceles == True:
        print('Triangulo isoceles')
    elif triangulo_escaleno == True:
        print('Triangulo Escaleno')