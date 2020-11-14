dicionario={'nome':'Pedro','idade':25}
print(dicionario['nome'])
print('-'*20)
dicionario['sexo']='M'
print(dicionario['sexo'])
print('-'*20)
del dicionario['idade']
print(dicionario)
print('-'*20)
filme={'titulo':'Star Wars','ano':1977,'diretor':'George Lucas'}
print(filme)
print('-'*20)
print(filme.values())
print(filme.keys())
print(filme.items())

for key,value in filme.items():
    print(f'O {key} é {value}')

filme2={'titulo':'Avengers','ano':2012,'diretor':'Joss Whedon'}
filme3={'titulo':'Matrix','ano':1999,'diretor':'Wachowski'}
locadora=[filme,filme2,filme3]
print(locadora[0]['ano'])
print(locadora[2]['titulo'])
print('-'*30)
estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigra do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for chave, valor in e.items():
        print(f'O campo {chave} tem valor {valor}.')
