import numpy as np

A = np. array([[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5],
              ])
a = np.squeeze(A)
x = np.array([[[0], [1], [2]]])
print(x, axis=0)

