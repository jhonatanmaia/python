a=int(input('Enter the velocity: '))

if a>80:
    b=(a-80)*7.0
    print('You received a traffic ticket! Value $ {:.2f}'.format(b))