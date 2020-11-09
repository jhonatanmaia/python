valorCasa=float(input('House Price: $'))
salario=float(input('Salary: $'))
tempo=int(input('How many years?'))

tempo_mes=tempo*12
calc_aprovacao=salario*0.3
casa_parcela=valorCasa/tempo_mes
x=round(casa_parcela,2)

if calc_aprovacao > casa_parcela:
    print('Aproved')
else:
    print('Refused')