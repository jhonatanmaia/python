'''
+ adição
- subtração
* multiplkicação
/ divisão
** potencia
// divisao inteira
% resto da divisao, modulo

() - sao executados primeiros
** - sao executados segundo
* / // % - sao executados por terceiro
+ - - sao executado por ultimo

print(25**(1/2))
print('oi'*5)
print('='*20)
nome=input('QUal é seu nome?')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te \n conhecer {:^20}!'.format(nome))
#para dar print e nao querbar a linha
print('Prazer em te conhecer {:=^20}!'.format(nome), end=' ')
print('Prazer em te conhecer {:>20}!'.format(nome))
'''