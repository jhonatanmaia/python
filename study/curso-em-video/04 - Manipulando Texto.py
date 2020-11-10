'''

String = cadeira de caracter = frase
Para cada caracter é denominado um indice começado em 0, sendo
o espaço é contado
maiusculo e diferenciado de minusculo

'''

frase='Teste para a video aula'
print(frase[9])
#ira ate o indice 12, o final é sempre -1
print(frase[9:15])
# imprime pulando de 2 em 2
print(frase[9:24:2])
# Começa indice 0 ate o indice 9
print(frase[:10])
# Começa no indice 10
print(frase[10:])
# Começa no 9, vai ate o final pulando de 3 em 3
print(frase[9::3])

# Analise de string

#tamanho da frase
print(len(frase))
#contar um caracter
print(frase.count('a'))
#contar um caracter entre um espaço
print(frase.count('a',0,15))
#Printa o indice de onde começa certo caracter
print(frase.find('au'))
#Se retornar -1 e porque nao existe
print(frase.find('Android'))
#Procura algo e retorna um bool
print('Aula' in frase)
#troca palavras
print(frase.replace('aula','Android'))
#Letra nao maiuscula para maiuscula
print(frase.upper())
#letra nao minuscula para minuscula
print(frase.lower())
print(frase.lower().find('aula'))
#Vai deixar o indice 0 maiusuclo e o resto tudo minusuclo
print(frase.capitalize())
#Vai deixar indice 0 de cada palavra maiusculo, indeitifica a palavra pelo espaço
print(frase.title())

frase2='   Aprenda Python  '
print(frase2)
#Remove espaços inuteis
print(frase2.strip())
#Remove so os ultimos espaços
print(frase2.rstrip())
#Remove so os primerios espaços
print(frase2.lstrip())

#divide a string pelo espaço e faz uma lista
#Possui outras funcionalidades
print(frase.split()) 
dividido=frase.split()
print(dividido[2][3])
#junção da lista
#print('-'.join(frase.split))

#imprimir um texto grande
print("""texto
      muito
      grande
      para
      ser
      impresso""")

#uma string e imutavel, porem:
print(frase)
frase.replace('aula','Python')
print(frase)
frase=frase.replace('aula','Python')
print(frase)