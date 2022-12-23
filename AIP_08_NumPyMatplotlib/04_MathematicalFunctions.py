import numpy as np

# 행렬곱과 원소끼리의 곱은 다름

a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
# print(a+b)            # 원소끼리 합
# print(a*b)            # 원소끼리 곱
# print(a@b)
# print(np.dot(a,b))    # 행렬 곱
# print(np.inner(a,b))  #  

a = np.array([-1.7, 11.5, -0.2, 0.6, 10])
b = np.around(a)  # 반올림
c = np.floor(a)   # 내림
d = np.ceil(a)    # 올림
# print('a: ', a)
# print('b: ', b)
# print('c: ', c)
# print('d: ', d)

a = np.array([1.0, 5.55, 123, 0.567, 25.532])
b = np.around(a)
c = np.around(a, decimals=1)
c2 = np.around(a, decimals=2)
d = np.around(a, decimals=-1)  # default : 0

print('a: ', a)
print('b: ',b)
print('c: ',c)
print('c2: ', c2)
print('d: ', d)
