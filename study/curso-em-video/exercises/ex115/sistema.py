import lib.interface as interface
import lib.arquivo as arquivo

arq='cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso')
    arquivo.criarArquivo(arq)

while True:
    resposta=interface.menu(['Listar Pessoas','Cadastrar Pessoas',
                             'Sair do Sistema'])
    if resposta==1:
        # Listar arquvio
        arquivo.lerArquivo(arq)
    elif resposta==2:
        interface.cabecalho('Novo Cadastro')
        nome=str(input('Nome: '))
        idade=interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq,nome,idade)
    elif resposta==3:
        print(interface.cabecalho('Saindo do Sistema'))
        break
    else:
        print('Erro, digite umma opção válida.')