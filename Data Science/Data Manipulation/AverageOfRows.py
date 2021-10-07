# Data Manipulation: Code Project
# Data Science - Average of Rows
import numpy as np
rows, cols = [int(x) for x in input().split()]
#list = [[1 for cols in range(cols)] for rows in range(rows)]

list=[]
for i in range(rows):
    list.append([float(y) for y in input().split()])
print(list)

#for rows in range(rows):
#    for cols in range(cols):
#        list[rows][cols]= float(input())
#print(list)
avg = np.mean(list, axis=1)
print(avg)
