a1=float(input('Primeira nota: '))
a2=float(input('Segunda nota: '))
media=(a1+a2)/2
if media<5.0:
    print('Reprovado')
elif media> 5.0 and media<6.9:
    print('Recuperação')
else:
    print('Aprovado')