import matplotlib.pyplot as plt
import math

xtab = []
fxtab = []
gxtab = []

for i in range(0, 314):
    x = float(i) / 100.0
    fx = math.sin(x)
    gx = math.exp(x) - 2.0
    xtab.append(x)
    fxtab.append(fx)
    gxtab.append(gx)

plt.plot(xtab, fxtab)
plt.plot(xtab, gxtab)
plt.show()