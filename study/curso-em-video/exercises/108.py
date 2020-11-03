import utilidadescev.moedas as m

p=float(input('Digite o preço: R$'))
print(f'A metade de {m.formatacao(p)} é {m.formatacao(m.metade(p))}')
print(f'O dobro {m.formatacao(p)} é {m.formatacao(m.dobro(p))}')
print(f'Aumentando 10%, temos {m.aumentar(p,10)}')