from typing import no_type_check


import numpy as np

rows, cols = [int(x) for x in input().split()]
X = []
for i in range(rows):
    X.append([float(x) for x in input().split()])

y = [float(x) for x in input().split()]

X = np.array(X).reshape(rows, cols)
y = np.array(y)
result=np.dot(np.linalg.pinv(X), y.transpose())
print(np.around(result, decimals=2))