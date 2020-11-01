def voto(ano_nascimento):
    from datetime import date
    ano_atual=date.today().year
    r=ano_atual-ano_nascimento
    if 16 <= r < 18 or r>65:
        return 'OPCIONAL'
    elif r<18:
        return 'NÃO VOTA'
    else:
        return 'OBRIGATÓRIO'

ano=int(input('Digite o seu ano de nascimento: '))
print(f'O seu voto é {voto(ano)}')