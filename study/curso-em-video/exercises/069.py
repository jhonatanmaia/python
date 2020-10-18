idade_maior_18_anos=homens_cadastrados=mulheres_menos_20_anos=0
while True:
    sexo=str(input('Digite o sexo: [M/F]')).strip().upper()
    #while sexo != 'M' and sexo != 'F':
    #    sexo=str(input('Digite o sexo: [M/F]')).strip().upper()
    while sexo not in 'MF':
        sexo=str(input('Digite o sexo: [M/F]')).strip().upper()
    idade=int(input('Digite a idade: '))
    while idade<0:
        idade=int(input('Digite a idade: '))
    if sexo == 'M':
        homens_cadastrados+=1
    if idade > 18:
        idade_maior_18_anos+=1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20_anos+=1
    saida=str(input('Deseja contiuar? [s/n]' )).strip().upper()
    if saida == 'N':
        break
print(f'Há {idade_maior_18_anos} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens_cadastrados} homens.')
print(f'Foram cadastradas {mulheres_menos_20_anos} mulheres com menos de 20 anos.')