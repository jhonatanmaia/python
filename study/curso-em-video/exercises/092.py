from datetime import date
ano_atual=date.today().year
pessoa={}
pessoa['nome']=str(input('Nome: '))
idade=int(input('Ano de Nascimento: '))
pessoa['idade']=ano_atual-idade
pessoa['ctps']=int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contrato']=int(input('Ano de Contratação: '))
    pessoa['salario']=int(input('Salário: $'))
    apo=35-(ano_atual-pessoa['contrato'])+(ano_atual-idade)
    pessoa['aposentadoria']=apo
print('-='*30)
print(pessoa)
for chave, valor in pessoa.items():
    print(f'{chave} tem o valor {valor}')