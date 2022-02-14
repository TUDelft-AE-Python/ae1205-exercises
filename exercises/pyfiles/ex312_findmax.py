a = float(input('Enter a value a: '))
b = float(input('Enter a value b: '))
c = float(input('Enter a value c: '))
d = float(input('Enter a value d: '))

# Find maximum of a and b
if a > b:
    m1 = a
else:
    m1 = b

# Find maximum of c and d
if c > d:
    m2 = c
else:
    m2 = d

# Print largest of all four values
if m1 > m2:
    print("The maximum value is:", m1)
else:
    print("The maximum value is:", m2)

# Doing the same in one line:
print("The maximum value is:", max(a, b, c, d))
