import numpy as np

arr = np.array([3, 4, 6, 10, 24, 89, 45, 43, 46, 99, 100])

# Not divisible by 3:
print('Elements not divisible by 3:', arr[arr%3 != 0])
# Divisible by 5:
print('Elements divisible by 5:', arr[arr%5 == 0])
# Divisible by 3 and 5:
print('Elements divisible by 3 and 5:', arr[(arr%3 == 0) * (arr%5 == 0)])
# Set elements that are divisible by 3 to 42
arr[arr%3 == 0] = 42
print('Our new array becomes:', arr)