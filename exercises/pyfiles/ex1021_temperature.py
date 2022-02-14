import numpy as np
import matplotlib.pyplot as plt

h = np.arange(0, 32.0, 1.0)

to11 = 288.15 - 6.5 * h
to20 = 216.65
to32 = 216.65 + 1.0 * (h - 20.0)

temp = (h < 11) * to11 + (h >= 11) * to20 + (h >= 20) * (to32 - to20)

plt.plot(h, temp)
plt.show()