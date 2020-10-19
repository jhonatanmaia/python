# https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2019
times_brasileiros=('Flamengo','Santos','Plameiras','Grêmio',
                  'Athletico Paranaense','São Paulo','Internacional',
                  'Corinthians','Fortaleza','Goiás','Bahia','Vasco da Gama',
                  'Atlético','Fluminense','Botafogo','Ceará','Cruzeiro',
                  'CSA','Chapecoense','Avaí')
print(f'Os cinco primeiros colocados são: {times_brasileiros[:5]}')
print(f'Os quatro últimos colocados são: {times_brasileiros[-4:]}')
print(f'Os times em ordem aflabética: {sorted(times_brasileiros)}')
print(f'O Chapecoense está na posição: {times_brasileiros.index("Chapecoense")}')
#print('O Chapecoense está na posição: {}'.format(times_brasileiros.index("Chapecoense")))