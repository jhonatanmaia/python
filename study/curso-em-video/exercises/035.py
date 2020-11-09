a1=float(input('Enter the first side: '))
a2=float(input('Enter the second side: '))
a3=float(input('Enter the third side: '))

if a1+a2>a3 and a1+a3>a2 and a2+a3>a1:
    print('A triangle can be formed')
else:
    print('It is impossible to creat a triangle')