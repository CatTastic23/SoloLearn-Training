# Data Manipulation: Code Project
# Data Science - Average of Rows
import numpy as np
rows, cols = [int(x) for x in input().split()]

list=[]
for i in range(rows):
    list.append([float(y) for y in input().split()])
print(list)

avg = np.mean(list, axis=1)
print(avg)
