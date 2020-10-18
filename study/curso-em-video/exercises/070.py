soma=produtos_mais_de_mil=preco_produto_caro=0
produto_mais_caro=''
while True:
    produto=str(input('Digite o nome do produto: ')).strip()
    valor_produto=float(input('Digite o valor do produto: $'))
    saida=str(input('Deseja continuar? [S/N] ')).strip().upper()
    while saida != 'S' and saida != 'N':
        saida=str(input('Deseja continuar? [S/N] ')).strip().upper()
    soma+=valor_produto
    if valor_produto > preco_produto_caro:
        produto_mais_caro=produto
    if valor_produto > 1000.0:
        produtos_mais_de_mil+=1
    if saida == 'N':
        break
print(f'Foi gasto {soma}€ nos produtos.')
print(f'Houve {produtos_mais_de_mil} produtos acima de 1000€.')
print(f'O produto mais caro foi {produto_mais_caro}.')