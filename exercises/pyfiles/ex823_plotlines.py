import matplotlib.pyplot as plt

plt.plot([3, 3], [-10, 3], color='k', linestyle='-', linewidth=2)
plt.plot([-10, 3], [3, 3], color='r', linestyle='-', linewidth=2)
plt.plot([-10, 3], [3, -10], color='b', linestyle='--', linewidth=2)

plt.show()