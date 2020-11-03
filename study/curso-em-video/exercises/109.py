import utilidadescev.moedas as m

p=float(input('Digite o preço: R$'))
print(f'A metade de {m.formatacao(p)} é {m.metade(p,False)}')
print(f'O dobro de {m.formatacao(p)} é {m.dobro(p,True)}')
print(f'Aumentando 10%, temos {m.aumentar(p,10,True)}')
print(f'Reduzingo 13%, temos {m.diminuir(p,13,True)}')