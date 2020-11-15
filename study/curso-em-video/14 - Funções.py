'''
Funções = rotina
def = definição de função

def mostraLinha():
    print('-'*30)


mostraLinha()
print('Sistema de Alunos')
mostraLinha()

Os parametros passado pelo usuario sao os parametros reais
e os parametros da funcao sao os parametros formais

def mensagem(msg):
    print("-"*30)
    print(msg)
    print("-"*30)

def soma(a,b):
    s=a+b
    print(s)

soma(4,5)
Pode-se explicitar a entrada
soma(b=4,a=5)

-> Empacotamento de parametros
def contador(*num):

def contador(* num):
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todos {tam} números')
    for valor in num:
        print(f'{valor} ',end='')
    print('FIM')


contador(1,2,3,4,5,6)
def divisao(a,b):
    print(a/b)


divisao(1,4)
def soma(a,b):
    print(a+b)
    
# A função pode receber uma lista em vez de ser um dic
def dobra(lit):
    pos=0
    while pos<len(lit):
        lit[pos]*=2
        pos+=1

lista=[7,2,4,0,4]
dobra(lista)
print(lista)


# INTERACTIVE HELP
help(print) #Mostra toda documentação da função
# Pode ser usado apenas help() no console, para sair use o quit
print(input.__doc__) # outra forma de se fazer
'''

#DOCSTRING
# O manual para cada função
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c=i
    while c<=f:
        print(f'{c}',end='..')
        c+=p
    print('FIM')


help(contador)

# Parametros Opcionais
def somar(a,b,c=0):
    # Se o valor de c não for passado então c vai assumir o valor de 0
    s=a+b+c
    print(f'A soma vale {s}')


somar(2,3)

def somar2(a=0,b=0,c=0):
    s=a+b+c
    print(f'A soma vale {s}')
    

# Escopo de Variáveis
def teste(b):
    # Tudo declarado dentro da função e variavel local
    # Não podera ser chamada fora dela
    global a
    a=8
    # para a dentro da função ser o a global, deve se dizer global antes
    b+=4
    c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Area global das variaveis
a=5
teste(a)
print(f'A fora vale {a}')

def somar3(a=0,b=0,c=0):
    s=a+b+c
    return s
    