'''

Codigo ANSI para cores

\033[estilo;texto;cordefundobackgroundm]
\033[0;33;44m]
estilo
0 - none
1 - bold negrito
4 - underline sublinhar
7 - negative negativo
texto
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 roxo
36 azul piscina
37 cinza - padrao
fundo
40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 roxo
46 azul piscina
47 padrao

'''
from colorama import Fore, Back, Style
print('\033[1;31;47mTeste\033[m')
print('\033[0;30;47mTeste\033[m')
print('texto {}'.format(Fore.GREEN+Back.BLACK+'Teste'))