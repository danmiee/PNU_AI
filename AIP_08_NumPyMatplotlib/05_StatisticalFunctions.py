import numpy as np

a = np.array([[3, 7, 5],
              [8, 4, 3],
              [2, 4, 9]])
b = np.amin(a, 1)  # 열에서 최소값
c = np.amin(a, 0)  # 행에서 최소값
d = np.amin(a)    # 배열에서 최소값
e = np.amax(a, 1)
f = np.amax(a, 0)
print('a \n', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print('e: ', e)
print('f: ', f)
