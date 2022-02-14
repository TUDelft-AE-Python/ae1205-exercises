Ra = float(input("What is the resistance of resistor A?"))
Rb = float(input("What is the resistance of resistor B?"))
Rc = float(input("What is the resistance of resistor C?"))

Rab = (1.0 / Ra + 1.0 / Rb) ** -1

Rabc = Rab + Rc
print(Rabc)