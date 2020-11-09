x=int(input('Enter the number to convert: '))
print('Select the convertion')
print(''' 
[ 1 ] Binary
[ 1 ] Octal
[ 3 ] HexaDeicmal
''')
y=int(input('1 - Binary 2 - Octal 3 - Hexadecimal'))

if y==1:
    bin(x)[2:]
    print('{}'.format(x))
elif y==2:
    oct(x)
    print('{}'.format(x))
elif y==3:
    hex(x)
    print(x)
else:
    print('Invalid')