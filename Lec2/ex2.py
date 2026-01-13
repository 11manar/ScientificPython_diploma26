import numpy as np
import time

start = time.time()
a = [ [1, 2, 3], [4, 5, 6], [2, 7, 9] ]
b = [ [7, 8, 9], [10, 11, 12], [3, 0, 4] ]

c = [[0]*3 for i in range(3)]

for i in range(3):
  for k in range(3):
    for j in range(3):
      c[i][k] += a[i][j] * b[j][k]

end = time.time()
print(c)
print("time = ", end - start)

start = time.time()
a = np.array([ [1, 2, 3], [4, 5, 6], [2, 7, 9] ])
b = np.array([ [7, 8, 9], [10, 11, 12], [3, 0, 4] ])
print('Matrix product\n', np.matmul(a,b))
end = time.time()
print("time = ", end - start)
