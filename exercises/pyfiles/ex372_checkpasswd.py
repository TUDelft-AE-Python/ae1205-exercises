password = input("Enter a password: ")

abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%&*+-=?^_~"

length_indicator = False
abc_indicator = False
ABC_indicator = False
digits_indicator = False
special_indicator = False

# check length
if len(password) >= 8 and len(password) <= 16:
    length_indicator = True

# go over the password and check for each character
for char in password:
    if char in abc:
        abc_indicator = True
    if char in ABC:
        ABC_indicator = True
    if char in digits:
        digits_indicator = True
    if char in special:
        special_indicator = True
    # we can add a break to speed things up
    if abc_indicator and ABC_indicator and digits_indicator and special_indicator:
        break

# if all indicators are True, the password is valid
if length_indicator and abc_indicator and ABC_indicator and digits_indicator and special_indicator:
    print("Valid password")
else:
    print("Invalid password")