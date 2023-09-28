import numpy as np
arr = np.array([[10, 20, 4, 1, 22], [65, 33, 22,56, 12]])

small = arr[0][0]
largest  = arr[0][0]
for x in arr:
    for y in x:
        if y > largest:
            largest = y;
        elif y < small:
            small = y
            
print(f"largest is {largest}")
print(f"smallest is {small}")
