soma_idade=0
media_Idade=0
maior_idade_homem=0
nome_velho=''
tot_mulher_20=0
for i in range(0,4):
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo: ')).strip()
    soma_idade+=idade
    if i==1 and sexo in 'Mm':
        maior_idade_homem=idade
        nome_velho=nome
    elif sexo in 'Mm' and idade>maior_idade_homem:
        maior_idade_homem=idade
        nome_velho=nome
    if sexo in 'Ff' and idade <20:
        tot_mulher_20+=1
media_Idade=soma_idade/4
print(media_Idade)
print(maior_idade_homem,nome_velho)
print(tot_mulher_20())