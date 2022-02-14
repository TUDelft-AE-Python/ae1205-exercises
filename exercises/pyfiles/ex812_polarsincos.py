import matplotlib.pyplot as plt
import math


xtab = []
ytab = []

for i in range(0, 628):
    # Calculate polar coordinates for provided equation
    phi = float(i) / 100.0
    r = 4 * math.cos(2 * phi)
    # Convert to Cartesian and store in lists
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    xtab.append(x)
    ytab.append(y)

plt.plot(xtab, ytab)
plt.show()