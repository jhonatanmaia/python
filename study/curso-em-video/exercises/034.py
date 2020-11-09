a1=float(input('Enter the salary: $'))

if a1<1250:
    print('The new salary is: ${:.2f}'.format(a1*1.15))
else:
    print('THe new salary is: ${:.2f}'.format(a1*1.10))