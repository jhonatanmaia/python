print('='*30)
print('{:^30}'.format('Banco Vai Falir'))
print('='*30)
'''
saque=int(input('Introduza o valor a ser sacado: $'))
cedula_50=cedula_20=cedula_10=cedula_1=0
cedula_50=saque//50
cedula_20=(saque%50)//20
cedula_10=((saque%50)%20)//10
cedula_1=((saque%50)%20)%10
print(f'Total de {cedula_50} cédulas de R$50')
print(f'Total de {cedula_20} cédulas de R$20')
print(f'Total de {cedula_10} cédulas de R$10')
print(f'Total de {cedula_1} cédulas de R$1')
'''
valor=int(input('Que valor você quer sacar? R$'))
total=valor
ced=50
totced=0
while True:
    if total >= ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced==50:
            ced==20
        elif ced==20:
            ced==10
        elif ced==10:
            ced==1
        totced=0
        if total ==0:
            break