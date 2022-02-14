v_start = float(input("Enter the start amount: "))
interest = float(input("Enter the interest rate in percent: "))
nyears = int(input("For how many years do you want to calculate the interest? "))

# Calculate growth rate
rate = 1.0 + interest / 100.0

# Calculate compound interest: start with initial sum
v_end = v_start
for i in range(1, nyears + 1):
    # Each year we should multiply the accumulated sum with the
    # growth rate
    v_end = v_end * rate
    # Print the accumulated sum after each year
    print('Total sum after', i, 'years is:', v_end)