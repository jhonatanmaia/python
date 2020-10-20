produtos = ('Computador',1000.50,'Monitor',300.0,'Cadeira',120.0,
            'Mesa',50.0,'Cabo HDMI',8.5)
print('-'*38)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*38)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        # Formata para a direita
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'{produtos[pos]:>7.2f}€')
print('-'*38)