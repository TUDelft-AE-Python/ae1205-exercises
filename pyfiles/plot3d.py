from numpy import exp,arange,meshgrid,arange
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D

# Define the function that we're going to plot
def z_func(x, y):
    return (1 - (x**2 + y**3)) * exp(-(x**2+y**2) / 2)

# Make the mesh and the z-value 
x = arange(-3.0, 3.0, 0.1)
y = arange(-3.0, 3.0, 0.1)
X,Y = meshgrid(x, y) # grid of point
Z = z_func(X, Y) # evaluation of the function on the grid

# Create the 3D plot
fig = plt.figure()
ax = Axes3D(fig)

# 3D surface plot
#surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
#                      linewidth=0, antialiased=False)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
                    cmap=cm.RdBu,linewidth=0, antialiased=False)

# Legend
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show figure
plt.show()