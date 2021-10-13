import numpy as np
r = int(input())
lst = [float(x) for x in input().split()]
arr = np.array(lst).round(2)
div = int(len(arr)/r)
reshape = arr.reshape(r, div)
print(reshape)