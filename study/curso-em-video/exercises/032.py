from datetime import date

a1=int(input('Enter a year: '))

if a1==0:
    a1=date.today().year
if a1%400==0:
    print('It is a bye year')
elif a1%4==0 and a1%100 != 0:
    print('It is a bye year')
else:
    print('It is not a bye year')