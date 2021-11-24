from sklearn.metrics import confusion_matrix
import numpy as np

y_true = [int(x) for x in input().split()]
y_pred =  [int(x) for x in input().split()]

y_true = np.array(y_true)
y_true = y_true.astype(str)
y_pred = np.array(y_pred)
y_pred = y_pred.astype(str)

new_data = confusion_matrix(y_pred, y_true, labels=['1','0'])
new_data = new_data.astype('f')
print(new_data)