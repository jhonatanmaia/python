a=[]
for i in range(0,5):
    a.append(float(input('Digite o Peso: ')))
a.sort()
print('O maior peso foi {} e o menor foi {}'.format(a[4],a[0]))