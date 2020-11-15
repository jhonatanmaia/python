'''
-> Surgiu no inicio da decada de 60
-> Sistemas ficando cada vez maiores
-> Foco: dividir um programa grande
-> Foco: aumentar a legibilidade
-> Foco: Facilitar a manutenção

Vantagens
-> Organização do código
-> Facilidade na manuntenção
-> Ocutaçao de código detalhado
-> Reutilização em outros projetos
'''
import moduloAulaAnterior
  
n=int(input('Digite um valor: '))
fat=moduloAulaAnterior.fatorial(n)
print(f'O fatorial de {n} é {fat}')