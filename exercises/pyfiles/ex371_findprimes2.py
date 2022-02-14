maxvalue = int(input("Until which value do you want to calculate the prime numbers?"))

# The first prime, 2, we skip, so that afterwards we can make our loop faster by skipping all even numbers:
print("The prime numbers under", maxvalue, "are:")
print(2)

# Break as soon as isprime is False
for n in range(3, maxvalue + 1, 2):
    # Let's start out by assuming n is a prime:
    isprime = True
    # For each n we want to look at all values larger than one, and smaller than n:
    for x in range(2, n):
        # If n is divisible by x, the remainder of this division is 0. We can check this with the modulo operator:
        if n % x == 0:
            # If we get here the current n is not a prime.
            isprime = False
            # we don't need to check further numbers
            break
    # If isprime is still True this is indeed a prime
    if isprime:
        print(n)


# Alternative approach with for-else
for n in range(3, maxvalue + 1, 2):
    for x in range(2, n):
        if n % x == 0:
            # In this case we only need to break
            break
    else:
        # When this else block is reached n is a prime
        print(n)