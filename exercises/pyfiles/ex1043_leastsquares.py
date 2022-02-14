import numpy as np


''' By hand '''
x = np.arange(0.1, 1.1, 0.1)
y = 5 * np.exp(-x) + 2 * x

# Reshape x and y to obtain 2D vectors
# We want a linear trend, so y = b1 + b2x = Xb
# If b = [b1, b2], then X should be [[1, x_0], [1, x_1], ...]
X = np.ones((len(x), 2))
X[:,1] = x

Y = y.reshape((len(y), 1))

# Solve using b = (XTX)^-1XTY
XTXi = np.linalg.inv(X.T @ X)
XTY = X.T @ Y
b = XTXi @ XTY

# Print the result
print(b)



''' Using np.linalg '''
x = np.arange(0, 1.1, 0.1)
y = 5 * np.exp(-x) + 2 * x

X = np.ones((len(x), 2))
X[:,1] = x
Y = y.reshape((len(y), 1))

print(np.linalg.lstsq(X, Y))