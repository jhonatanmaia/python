a1=int(input('Enter the travel distance: '))

if a1<=200:
    a2=a1/2
    print('The travel price is: ${}'.format(a2))
else:
    a2=a1*0.45
    print('The travel price is: ${}'.format(a2))