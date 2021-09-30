from math import *
import matplotlib.pyplot as plt


# Switch on interactive mode
plt.ion()

for i in range(100):
    x = float(i) / 10.0
    plt.plot(x, sin(x), "ro")  # plot each point as a red dot
    plt.draw()  # Show result

plt.close()
