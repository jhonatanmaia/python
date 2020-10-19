numero_extenso=('zero','um','dois','trÃªs','quatro','cinco','seis',
                'sete','oito','nove','dez','onze','doze','treze',
                'catorze/quatorze','quinze','dezesseis','dezessete',
                'dezoito','dezenove','vinte')
while True:
    while True:
        numero=int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            print(f'Você digitou o número {numero_extenso[numero]}.')
            break
        else:
            print('Número incorreto.', end='')
            
    saida=str(input('Você deseja sair? [S/N] ')).strip().upper()
    while saida != 'S' and saida != 'N':
        saida=str(input('Você deseja sair? [S/N] ')).strip().upper()
    if saida == 'S':
        break