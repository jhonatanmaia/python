import utilidadescev.moedas as m

p=float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {m.metade(p)}')
print(f'O dobro de {p} é {m.dobro(p)}')
print(f'Aumentando 10%, temos {m.aumentar(p,10)}')
print(f'Reduzndo 13%, temos {m.diminuir(p,13)}')