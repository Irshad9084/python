import numpy as np
arr1= np.array([0,10,20,40,60])
arr2= np.array([0,40])
array([ True, False, False,  True,False], dtype=bool)
c = np.isin(arr1, arr2)
print(c)
