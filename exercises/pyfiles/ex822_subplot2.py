import matplotlib.pyplot as plt
import math

x1tab = []
y1tab = []
x2tab = []
y2tab = []

for i in range(0, 2513):
    theta = float(i) / 100.0

    r1 = theta
    r2 = theta**2

    x1 = r1 * math.cos(theta)
    y1 = r1 * math.sin(theta)

    x1tab.append(x1)
    y1tab.append(y1)

    x2 = r2 * math.cos(theta)
    y2 = r2 * math.sin(theta)

    x2tab.append(x2)
    y2tab.append(y2)

plt.subplot(121)
plt.plot(x1tab, y1tab)
plt.title("r = theta")
plt.xlabel("x")
plt.ylabel("y")
plt.subplot(122)
plt.plot(x2tab, y2tab)
plt.title("r = theta**2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()