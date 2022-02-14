import numpy as np
A = np.array([[2, -5, 6], [4, 3, 8], [5, -2, 9]])
b = np.array([[3, 5, -1]]).T # .T because we need a column vector
# Calculate x using the inverse of A
Ainv = np.linalg.inv(A)
x = Ainv.dot(b) # You can also use Ainv @ b