startsum = float(input("What is your starting amount to save?"))
nyears   = int(input("How many years do you want to save your money?"))
interest = float(input("What is the yearly interest rate (in percent)?"))
endsum = startsum * (1.0 + interest / 100.0) ** nyears
print(endsum)