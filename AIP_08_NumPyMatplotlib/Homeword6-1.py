# Exercises 1
import numpy as np

# a) 모든 요소가 2인 크기 6´4의 배열을 만듭니다.
a = np.ones((6, 4))*2
# a = np.ones(24).reshape(6,4)*2
print(a)

# b) 선행 대각선에 3개, 다른 곳에 1개 있는 크기 6´4의 배열 b를 만듭니다. (루프를 사용하지 마십시오.)
b = np.eye(6, 4)*2 + 1
print(b)

# c) 이 두 배열을 함께 곱할 수 있습니까? 그런 다음 a * b는 작동하지만 dot(a, b)는 작동하지 않는 이유를 설명하십시오.
print(a*b)
print(np.dot(a, b))
# a의 열 수와 b의 행 수가 같지 않으므로 행렬곱 계산인 np.dot(a*b)는 사용불가

# d) 점(a.transpose(), b) 및 점(a, b.transpose())을 계산합니다.
np.dot(a.transpose(), b)
np.dot(a, b.transpose())
# 결과가 다른 모양인 이유를 설명하시오.
# a.transpose() : 4*6, b : 6*4이므로 행렬곱은 4*4행렬
# a : 6*4, b.transpose() : 4*6이므로 행렬곱은 6*6행렬
