import numpy as np

a = np.array([[1, 2], [3, 4]])

# Manually
def printdiag(arr):
    # Use end=' ' to avoid the newline of print
    print('The numbers on the diagonal are:', end=' ')
    for i in range(len(arr)):
        print(arr[i,i], end=' ')
    # A final print for the newline
    print()


# Using a NumPy method
print('The numbers on the diagonal are:', a.diagonal())