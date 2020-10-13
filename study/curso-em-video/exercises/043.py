altura=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))
imc=round(peso/(altura**2),2)

if imc<18.5:
    print('Abaixo do Peso')
elif 18.5>imc<=25:
    print('Peso Ideal')
elif 25>imc<=30:
    print('Sobrepeso')
elif 30>imc<=40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')