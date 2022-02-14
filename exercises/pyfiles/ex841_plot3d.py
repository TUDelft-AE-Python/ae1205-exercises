import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Initialise our empty lists
X = []
Y = []
Z = []
for i in range(21):
    # Each row in X is just a row of all values of x:
    X.append(list(range(21)))
    # Each row in Y is n times the current value of y.
    # Our y increases with steps of 0.4
    Y.append(21 * [0.4 * i])
    # Our Z-values in the row depend on x:
    Zrow = []
    for x in range(21):
        Zrow.append(x**2 / 1000)
    Z.append(Zrow)

            

# Create a figure, with 3D axes:
fig = plt.figure()
ax = Axes3D(fig)

# Plot the data using Axes3D.plot_surface()
ax.plot_surface(X, Y, np.array(Z), rstride=1, cstride=1, linewidth=0, antialiased=False)
plt.show()



## All Numpy:
x = np.arange(0, 21, 1)
y = np.linspace(0, 8, 21)
X, Y = np.meshgrid(x, y)
Z = X**2 / 1000

# Create a figure, with 3D axes:
fig = plt.figure()
ax = Axes3D(fig)

# Plot the data using Axes3D.plot_surface()
ax.plot_surface(X, Y, np.array(Z), rstride=1, cstride=1, linewidth=0, antialiased=False)
plt.show()