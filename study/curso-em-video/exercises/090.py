aluno={}
aluno['nome']=str(input('Nome: '))
aluno['media']=float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 7.0:
    aluno['situacao']='Reprovado'
elif 5 <= aluno['media'] <7:
    aluno['situacao']='Recuperação'
else:
    aluno['situacao']='Aprovado'
    
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
    
print(f'O nome é igual a {aluno["nome"]}.')
print(f'A média é igual a {aluno["media"]}.')
print(f'A situação é: {aluno["situacao"]}')