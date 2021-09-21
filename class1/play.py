import numpy as np

arr = np.array(
    [12, 2, 40, 54, 5, 798, 45, 23]
)
print(arr[1:5])     # [ 2 40 54  5]
print(arr[3:-2])    # [ 54   5 798]
print(arr[:3])      # [12  2 40]
print(arr[:-2])     # [ 12   2  40  54   5 798]
print(arr[3:])      # [ 54   5 798  45  23]
print(arr[-3:])     # [798  45  23]
