# Exercises 3
import random
import numpy as np

# a) np.ones를 사용하여 4´4 배열 a를 만들고
a = np.ones((4, 4))
print(a)
# np.eye를 사용하여 또 다른 4´4 배열 b를 만들고
b = np.eye(4, 4)
print(b)
# 각각 4개의 숫자로 구성된 목록인 4개의 요소가 있는 목록 c.
c = [list(np.random.randint(0, 10, size=(4))) for _ in range(4)]
c = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
print(c)
# 지금, sum_=a + b 및 sub=a – c를 실행한 다음 sum_의 평균을 계산합니다.
# 합집합_. (참고: 변수 이름 sum_을 사용하는 이유는 sum이 변수의 이름이기 때문입니다. 파이썬 라이브러리 함수.)
sum_ = a + b
print(sum_)
sub = a - c
print(sub)
np.mean(sum_)

# b) 배열을 수신하고 1의 갯수를 세는 함수 findOne을 정의합니다.
def findOne(m):
  rows, cols = m.shape
  cnt = 0
  for r in range(rows):
    for c in range(cols):
      if m[r, c] == 1:
        cnt += 1
  print('Num ones: {}'.format(cnt))
# 임의의 정수로 구성된 5´5 배열을 만들고
m = np.random.randint(0, 10, size=(5, 5))
print(m)
# findOne을 사용하여 그 안에 있는 것들의 수를 세십시오.
findOne(m)
# where()' 함수를 사용하여 동일한 작업을 수행합니다.
A,_ = np.where(m == 1)
print(len(A))
# 넘파이. (참고: 사용 방법을 알아보려면 help(np.where)를 사용하세요.)

# l[1][2]
l=[[1,2,3],[4,5,6]]
