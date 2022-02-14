import matplotlib.pyplot as plt
import numpy as np


# Create our circle:
r = 2
phi1 = np.linspace(0, 2 * np.pi, 200)
x1 = r * np.sin(phi1)
y1 = r * np.cos(phi1)

# A hexagon is no more than a circle drawn with just 6 points:
phi2 = np.linspace(0, 2 * np.pi, 6)
x2 = r * np.sin(phi2)
y2 = r * np.cos(phi2)

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()