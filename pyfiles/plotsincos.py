from math import sin, cos, pi
import matplotlib.pyplot as plt


print('Welcome to my first plotting program')
print('This program will plot one period of the sine and cosine function in one graph')

# Definition of our step size delta x, and the number of datapoints:
n = 100
step = 2.0 * pi / n

# Initialisation of x and y value lists
xtab = []
y1tab = []
y2tab = []

# Note how we use an integer range function to generate floats
# Since the range function omits the final value given as end, we add 1
# to make sure our last value for x is exactly 2*pi
for i in range(n + 1):
    x = i * step
    y1 = sin(x)
    y2 = cos(x)

    xtab.append(x)
    y1tab.append(y1)
    y2tab.append(y2)

# Plot the sine and cosine lines in a graph
plt.plot(xtab, y1tab)
plt.plot(xtab, y2tab)

# Add a title, axis labels, and a legend
plt.title('One period of the sine and cosine functions')
plt.xlabel('x [rad]')
plt.ylabel('y')
plt.legend(('sin(x)', 'cos(x)'))

# Don't forget to call show()!
plt.show()
