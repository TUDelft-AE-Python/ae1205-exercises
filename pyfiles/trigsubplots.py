from math import sin, cos, tan, sinh, cosh, tanh, pi
import matplotlib.pyplot as plt

# First initialise the variables
# We want to go from -2pi to 2pi in 1000+1 steps
n = 1000
start = -2.0 * pi
step = 4.0 * pi / n

xtab = []
y1tab = []
y2tab = []
y3tab = []

y4tab = []
y5tab = []
y6tab = []

# Then generate the data
for i in range(n + 1):
    x = start + i * step

    xtab.append(x)
    y1tab.append(sin(x))
    y2tab.append(cos(x))
    y3tab.append(tan(x))
    y4tab.append(sinh(x))
    y5tab.append(cosh(x))
    y6tab.append(tanh(x))

# Generate the plots
# Make 2 rows of 3 graphs, start with plot 1
plt.subplot(231)
plt.plot(xtab, y1tab)
plt.title('sin')

plt.subplot(232)
plt.plot(xtab,y2tab)
plt.title('cos')

plt.subplot(233)
plt.plot(xtab,y3tab)
plt.axis([-2.0 * pi, 2.0 * pi, -5.0, 5.0]) # setting scale:xmin,xmax,ymin,ymax
plt.title('tan')

# Second row: plot 4-6
plt.subplot(234)
plt.plot(xtab, y4tab)
plt.title('sinh')

plt.subplot(235)
plt.plot(xtab, y5tab)
plt.title('cosh')

plt.subplot(236)
plt.plot(xtab, y6tab)
plt.title('tanh')

# Show plot window
plt.show()
