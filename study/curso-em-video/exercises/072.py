numero_extenso=('zero','um','dois','três','quatro','cinco','seis',
                'sete','oito','nove','dez','onze','doze','treze',
                'catorze/quatorze','quinze','dezesseis','dezessete',
                'dezoito','dezenove','vinte')
while True:
    while True:
        numero=int(input('Digite um n�mero entre 0 e 20: '))
        if 0 <= numero <= 20:
            print(f'Voc� digitou o n�mero {numero_extenso[numero]}.')
            break
        else:
            print('N�mero incorreto.', end='')
            
    saida=str(input('Voc� deseja sair? [S/N] ')).strip().upper()
    while saida != 'S' and saida != 'N':
        saida=str(input('Voc� deseja sair? [S/N] ')).strip().upper()
    if saida == 'S':
        break