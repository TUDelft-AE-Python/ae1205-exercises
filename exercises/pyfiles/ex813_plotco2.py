import matplotlib.pyplot as plt


time = list(range(1950, 2020, 10))
co2 = [250, 265, 272, 280, 300, 320, 389]

plt.plot(time, co2)
plt.show()