jogador={}
cadastro=[]
gols_marcados=[]
soma=gols=0
while True:
    print('-'*30)
    jogador['nome']=str(input('Nome do Jogador: '))
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0,partidas):
        gols_marcados.append(int(input(f'Quantos gols na partida {i}? ')))
        soma+=gols_marcados[i]
    jogador['gols']=gols_marcados[:]
    gols_marcados.clear()
    jogador['total']=soma
    cadastro.append(jogador.copy())
    soma=0
    sair=str(input('Deseja sair? [S/N] ')).upper()
    if sair == 'S':
        break
print('-='*30)
print(f'{"cod"} {"nome"} {"gols":>10} {"total":>19}')
print('-'*40)
for i in range(0,len(cadastro)):
    # Deveria centralizar
    print(f'  {i} {cadastro[i]["nome"]:<10} {cadastro[i]["gols"]} {cadastro[i]["total"]:>10}')
print('-'*40)
print('999 sai.')
while True:
    numero=int(input('Mostrar dados de qual jogador? '))
    print(f'-- LEVANTAMENTO DO JOGADOR {cadastro[numero]["nome"]}:')
    if numero == 999:
        break
    if numero > len(cadastro):
        print('Erro')
        continue
    for k in range(0,len(cadastro[numero]['gols'])):
        print(f'   No jogo {k} fez {cadastro[numero]["gols"][k]}')
# {v["Gols"]!s:<15s}