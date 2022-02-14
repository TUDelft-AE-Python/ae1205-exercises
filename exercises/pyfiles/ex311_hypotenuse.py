from math import sqrt

a = float(input("Enter the length of right side a: "))
b = float(input("Enter the length of right side b: "))

# Option 1
c = sqrt(a * a + b * b)
# Option 2
c = (a**2 + b**2)**0.5

print("The length hypotenuse c is", c)