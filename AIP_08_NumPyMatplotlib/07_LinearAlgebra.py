import numpy as np

a = np.array([[10,20],[30,40]])
b = np.array([[-4],[1]])

inv_a = np.linalg.inv(a)  # a의 역행렬
c = np.linalg.solve(a,b)  # ax=b의 x
d = np.linalg.det(a)      # a의 determinant
e = np.linalg.eig(a)      # a의 고유값과 고유벡터

print(inv_a)
print(c)
print(d)
print(e)