'''

https://docs.python.org/3/library/index.html

https://pypi.org/

Para importar toda a biblioteca 
import nomeBiblioteca

Para importar uma função especifica
from nomeBiblioteca import funcao
from nomeBiblioteca import funcao1,funcao2
from nomeBiblioteca import *

Para importar e dar um nome

import nomeBiblioteca as nomeMetodo
from nomeBiblioteca import funcao as nomeMetodo

Exemplo:
    import math
    from math import sqrt
    from math import sqrt as raizQuadrada
    
'''

import math
a1=int(input("Enter a number: "))
print("The squareroot of {} is {:.2f}, and roundend up is {}".format(a1,math.sqrt(a1),math.ceil(math.sqrt(a1))))


from math import sqrt, floor
a2=int(input("Enter a number: "))
print("The sqrt of {} is {}".format(a2,floor(sqrt(a2))))

import emoji
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize(" :musical_note:",use_aliases=True))