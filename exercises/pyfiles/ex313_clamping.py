# Approach 1: using if-else-statements:
a = float(input("Enter a value: "))

minimum = -10.0
maximum = 10.0

if a < minimum:  # too small
    a = minimum
elif a > maximum:  # too big
    a = maximum
else:
    pass  # means 'do nothing'

print(a)

if a < 0:
    print("The value is negative!")


# Approach 2: using min and max:
a = float(input("Enter a value: "))

minimum = -10.0
maximum = 10.0

# max(a, minimum) clamps the lower bound
# min(..., maximum) then immediately clamps the upper bound
a = min(max(a, minimum), maximum)

print(a)

if a < 0:
    print("The value is negative!")