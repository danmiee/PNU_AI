import numpy as np

a = np.arange(6)
print(a)

b = a.reshape(3, 2)  # reshape 시 원소 갯수가 동일하도록 주의
print(b)
print(b[2,1])
print(b[:,1])
print(np.shape(b))      # 행렬형태
print(np.size(b))
print(np.ndim(b))
print(np.transpose(b))  # 전치행렬

c = np.copy(b)  # deep copy
print(c)
print(np.ravel(c))  # 원소를 1차원으로 나열