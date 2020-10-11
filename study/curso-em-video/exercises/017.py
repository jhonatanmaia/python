import math

a1=float(input("Perendicular: "))
a2=float(input("Base: "))

print("Hypotenuse is {}".format(math.sqrt(a1**2 + a2**2)))
print("Hypotenuse is {}".format(math.hypot(a1,a2)))