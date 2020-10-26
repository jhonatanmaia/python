pessoa={}
cadastrados=[]
media_idade=0
mulheres=[]
acima_da_media=[]
while True:
    pessoa['nome']=str(input('Nome: '))
    pessoa['sexo']=str(input('Sexo [M/F]: ')).strip().upper()
    pessoa['idade']=int(input('Idade: '))
    media_idade+=pessoa['idade']
    cadastrados.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())
    sair=str(input('Você deseja sair?[S/N] ')).strip().upper()
    if sair == 'S':
        break
print(cadastrados)
media_final=media_idade/len(cadastrados)
print(f'Foram cadastradas {len(cadastrados)} pessoas')
print(f'A média de idade foi {media_final:.2f}')
print('As mulheres cadastradas foram: ',end='')
for i in range(0,len(mulheres)):
    print(f'{mulheres[i]["nome"]}',end=' ')
print()
for j in range(0,len(cadastrados)):
    if cadastrados[j]['idade']>media_final:
        acima_da_media.append(cadastrados[j])
print('As pessoas acima da media foram:')
for k in range(0,len(acima_da_media)):
    print(f'Nome = {acima_da_media[k]["nome"]};Sexo = {acima_da_media[k]["sexo"]}; Idade = {acima_da_media[k]["idade"]}')