import numpy as np
import matplotlib.pyplot as plt

# First create our x array
x = np.arange(-3, 3, 0.001)
# Then create our discontinuous function
# with masks for x <= 1 and x > 1
fx = (x<=1) * x**2 + (x>1) * (6 - x)

plt.plot(x, fx)
plt.show()