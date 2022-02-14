''' Slicing lists '''
lst = [[1, 2], [3, 4]]

# Get the first column, start with an empty one
col = []
# Iterate over all rows in our nested list, and add
# the first element to col to recreate the entire
# first column
for row in lst:
    col.append(row[0])


''' Slicing arrays '''
import numpy as np

arr = np.array([[1, 2], [3, 4]])
col = arr[:,0]