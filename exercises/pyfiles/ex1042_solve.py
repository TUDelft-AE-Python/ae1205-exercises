import numpy as np
A = np.array([[1, -1], [1, 1]])
b = np.array([[29.5 / 3.16667, 29.5 / 2.1]]).T # .T because we need a column vector
# Calculate x using the inverse of A
Ainv = np.linalg.inv(A)
x = Ainv.dot(b) # You can also use Ainv @ b
# Print the results
print('The motorboat speed is', x[0], 'km/h')
print('The current speed is', x[1], 'km/h')