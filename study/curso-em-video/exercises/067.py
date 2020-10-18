print('Digite um valor negativo para sair.')
while True:
    print('-'*40)
    tabuada=int(input('Qual tabuada você deseja? '))
    print('-'*40)
    if tabuada < 0:
        break
    for i in range(1,11):
        print(f'{tabuada} x {i} = {tabuada*i}')