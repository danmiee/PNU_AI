# Exercises 2
import numpy as np
# 주택 가격과 가격에 영향을 미치는 매개변수에 대한 일부 데이터가 있습니다.

# a) 위의 표와 같은 데이터를 가지는 배열 X를 만듭니다
data = [[1, 2104, 5, 1, 45, 460],
        [1, 1416, 3, 2, 40, 232],
        [1, 1544, 3, 2, 30, 315],
        [1, 852, 2, 1, 36, 178]]
X = np.array(data)
print(X)
#   X 모양: (4, 6).
#   assert () 함수를 사용하여 X의 모양이(4, 6)인지 확인합니다.
# (참고: assert(cond)는 cond가 True가 아니면 오류를 발생시킵니다.)
print(X.shape)
assert X.shape == (4, 6), "(4, 6) 모양이 아닙니다."

# b) 그런 다음 4개의 매개변수(크기, 침실 수, 층수, 집 나이)를 추출합니다.
# X를 새로운 행렬 P에 넣습니다. 다음을 통해 P의 모양이(4, 4)인지 확인합니다.
P = X[:, 1:5]
print(P)
# assert () 함수를 사용합니다.
print(P.shape)
assert P.shape == (4, 4), "(4,4) 모양이 아닙니다."

# c) numpy mean 함수를 사용하여 각 매개변수의 평균값을 찾습니다.
mean_value = np.mean(P, axis=0)
print(mean_value)

# P2 = P.transpose()
# c0 = np.mean(P2[0])
# c1 = np.mean(P2[1])
# c2 = np.mean(P2[2])
# c3 = np.mean(P2[3])
# print(c0)
# print(c1)
# print(c2)
# print(c3)
