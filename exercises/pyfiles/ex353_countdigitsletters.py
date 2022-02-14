print('Hello! This is a program that counts the number of digits and letters in a string you provide.')
text = input('Give your string: ')
# counters for the digits and letters
digits = 0
letters = 0
# We can loop directly over the characters in 'text'
for c in text:
    # Check if c is a digit
    if c.isdigit():
        digits = digits + 1

    # Else check if c is a letter
    elif c.isalpha():
        letters = letters + 1

# After the loop print the results:
print('Your string has', digits, 'digits, and', letters, 'letters!')
