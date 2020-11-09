a1=int(input('Enter a number: '))
a2=int(input('Enter a second number: '))
a3=int(input('Enter a third number: '))

if a1>a2 and a1>a3:
    print('{} is the highest number'.format(a1))
elif a2>a1 and a2>a3:
    print('{} is the highest number'.format(a2))
elif a3>a1 and a3>a2:
    print('{} is the highest number'.format(a3))