import numpy as np

n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])

X = np.array(X).reshape(-1,2)
centroid1 = np.array([0.,0.])
centroid2 = np.array([2.,2.])

for i in range(n):
    dist1 = np.sqrt(((X[i]-centroid1[0])**2).sum())
    dist2 = np.sqrt(((X[i]-centroid2[0])**2).sum())

    if(dist1 <= dist2):
        centroid1 = np.vstack((centroid1, X[i]))
    else:
        centroid2 = np.vstack((centroid2, X[i]))

if centroid1.size > 2:
   mean1 = np.mean(centroid1[1:], axis=0)
   print(np.around(mean1, decimals=2))
else:
   print(None)
      
   
if centroid2.size > 2:
   mean2 = np.mean(centroid2[1:], axis=0)
   print(np.around(mean2, decimals=2))
else:
   print(None)
