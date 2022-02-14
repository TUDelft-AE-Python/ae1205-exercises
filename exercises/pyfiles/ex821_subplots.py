import matplotlib.pyplot as plt
import math


y1tab = []
y2tab = []
xtab = []
for x in range(1000):
    x = x / 100.0
    xtab.append(x)

    y1 = math.cos(3.0 * x) + 2.0 * math.sin(2.0 * x)
    y1tab.append(y1)

    y2 = math.exp(-2.0 * x) + math.exp(-3.0 * x + 1.0)
    y2tab.append(y2)

plt.subplot(211)
plt.plot(xtab, y1tab)
plt.subplot(212)
plt.plot(xtab, y2tab)
plt.show()