def leiaDinheiro():
    txt=str(input('Digite um valor R$')).strip()
    while True:
        txt.replace('.',',')
        try:
            int(txt)
            return float(txt)
            break
        except ValueError:
            try:
                float(txt)
                return float(txt)
                break
            except ValueError:
                txt=str(input('Digite um valor R$')).strip()

'''
def leiaDinheiro(msg)
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mEROO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido= True
            return float(entrada)

solução sem o tratemtno de 
porem nao consegue diferenciar numeros e letras como 400f ou R$200
'''