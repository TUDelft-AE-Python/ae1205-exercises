import matplotlib.pyplot as plt
import math

# Constants and initial values
t = 0.0    #[s] time starts at zero
dt= 0.1  #[s]  time step
vy1 = 0.0  #[m/s] starting speed w/o drag
vy2 = 0.0  #[m/s] starting speed w drag
y1 = 10.0   #[m]  start altitude w/o drag
y2 = 10.0   #[m]  start altitude w drag
g = 9.81   #[m/s2] gravity acceleration
m = 2.0    #[kg]  mass
CD = 0.47  # Drag coefficient
rho = 1.225  # air density [kg/m3]
S = math.pi*0.15**2  # Effective surface [m2]

# We'll store our values in lists for later plotting
ttab = []
y1tab = []  # y1 without drag
y2tab = []  # y2 with drag

while y1 > 0 or y2 > 0:
    t = t + dt
    F = m * g
    D = 0.5 * CD * rho * vy2 ** 2 * S
    # Without drag
    a1 = (-1.0 * F) / m
    vy1 = vy1 + a1 * dt
    y1 = y1 + vy1 * dt

    # With drag
    a2 = (-1.0 * F + D) / m
    vy2 = vy2 + a2 * dt
    y2 = y2 + vy2 * dt

    ttab.append(t)
    y1tab.append(y1)
    y2tab.append(y2)

plt.plot(ttab, y1tab)
plt.plot(ttab, y2tab)
plt.show()