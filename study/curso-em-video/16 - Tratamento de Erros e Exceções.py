'''
Erros e Exceções
NameError -> Variavel não declarada ou nome escrito errado
ValueError -> Variável recebeu recebeu algo diferente, tipo int recebe str
ZeroDivisionError -> Divisão por zero
TypeError -> Erro de tipo, str ou int
IndexError -> Erro de index, acessar um index que não existe
KeyError -> Igual a IndexError porém é para dicionários
ModuleNotFoundError -> Modulo não achado

try:
    operação que dararia problemas que deve temtar
except:
    se falhou em try tente isso
else: -> Opcional
    se try deu certo, faça isso
finally: -> Opcional
    acontece mesmo quando da certo ou da errado
    
'''
try:
    a=int(input('Numerador: '))
    b=int(input('Denominador: '))
    r = a / b
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro: #joga a exceção para error
    print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')