for i in range(-4, 5):
    x = 5 - abs(i)
    # Print string of 'x' stars.
    # Remember that 'num * list' creates a combined
    # list with num times list joined together:
    print(x * '* ')

# Or with a nested loop:
for i in range(-4, 5):
    for j in range(5 - abs(i)):
        # To avoid the newline that is normally added by print, use the 'end' keyword argument:
        print('* ', end='')
    print()  # Add the newline after each finished nested loop