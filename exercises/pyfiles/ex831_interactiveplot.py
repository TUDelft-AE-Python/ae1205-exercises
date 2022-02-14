import matplotlib.pyplot as plt

plt.ion()

for x in range(-20, 20):
    x = float(x) / 10.0
    y1 = (2**2 - x**2) ** 0.5
    y2 = -(2**2 - x**2) ** 0.5

    plt.plot(x, y1, 'ro')
    plt.plot(x, y2, 'ro')
    plt.draw()

plt.close()