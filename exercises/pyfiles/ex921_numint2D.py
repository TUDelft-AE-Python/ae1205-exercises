import matplotlib.pyplot as plt
import math

''' Without Drag '''
delta = 0.01
s = 0
h = 1.0
theta = 30.0 * math.pi / 180.0
vx = 100 * math.cos(theta)
vy = 100 * math.sin(theta)
g = 9.81
stab = []
htab = []
while h >= 0:
    # Acceleration only dependent on gravity
    ay = -1.0 * g
    ax = 0

    vy = vy + ay * delta
    vx = vx + ax * delta

    h = h + vy * delta
    s = s + vx * delta

    htab.append(h)
    stab.append(s)

plt.plot(stab, htab)
plt.ylim(0, 140)
plt.show()


''' With constant drag '''
delta = 0.01
s = 0
h = 1.0
theta = 30.0 * math.pi / 180.0
vx = 100 * math.cos(theta)
vy = 100 * math.sin(theta)
g = 9.81
Fd = 80
m = 10
stab = []
htab = []
while h >= 0:
    # Acceleration dependent on gravity
    # and constant drag
    ay = (-1 * m * g -1 * Fd * math.sin(theta)) / m
    ax = (-1 * Fd * math.cos(theta)) / m

    vy = vy + ay * delta
    vx = vx + ax * delta

    h = h + vy * delta
    s = s + vx * delta

    theta = math.atan(vy / vx)

    htab.append(h)
    stab.append(s)

plt.plot(stab, htab)
plt.ylim(0, 140)
plt.show()


''' With aerodynamic drag '''
delta = 0.01
s = 0
h = 1.0
theta = 30.0 * math.pi / 180.0
vx = 100 * math.cos(theta)
vy = 100 * math.sin(theta)
g = 9.81
CD = 0.47
rho = 1.225
R = 0.15
S = math.pi * R**2
m = 10
stab = []
htab = []
while h >= 0:
    # Calculate the actual drag
    V2 = (vx**2 + vy**2)
    V = math.sqrt(V2)
    D = 0.5 * CD * rho * V2 * S
    # Decompose in x/y components,
    # making use of the ratio between vx and vy
    Dx = -D * vx / V
    Dy = -D * vy / V
    # Acceleration dependent on gravity
    # and drag
    ay = (-1 * m * g + Dy) / m
    ax = Dx / m

    vy = vy + ay * delta
    vx = vx + ax * delta

    h = h + vy * delta
    s = s + vx * delta

    htab.append(h)
    stab.append(s)

plt.plot(stab, htab)
plt.ylim(0, 140)
plt.show()