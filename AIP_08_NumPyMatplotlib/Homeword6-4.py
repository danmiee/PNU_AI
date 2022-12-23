# Exercises 4
import numpy as np
import matplotlib.pyplot as plt

# a) np.arange(-2, 2, 0.01)를 사용하여
# 시그모이드 함수 σ(x)=1 / (1 + e–x)를 플로팅합니다.
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))
# def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

x = np.arange(-2, 2, 0.01)
print(x)
y = sigmoid(x)
print(y)

plt.plot(x, y)
plt.title('Sigmoid')
plt.grid()
plt.show()

# b) 두 개의 텍스트 파일에 기록된 일부 실험 결과 데이터가 제공됩니다.
# "tError.txt" 및 "vError.txt", 여기에 하나의 부동 숫자가 있습니다.
# 각 라인. 단일 그래프에 두 데이터를 플로팅합니다.
f1 = open('.\\AIP_08_NumPyMatplotlib\\vError.txt', 'r')
v1 = [eval(line.rstrip()) for line in f1]
f1.close()

f2 = open('.\\AIP_08_NumPyMatplotlib\\tError.txt', 'r')
v2 = [eval(line.rstrip()) for line in f2]
f2.close()

print(v1)
print(v2)

# 가로축과 세로축 각각 '모델 복잡성'과 '오류율'을 나타냅니다.
plt.plot(v1)
plt.plot(v2)
plt.xlabel('Model Complexity')
plt.ylabel('Error Rate')
plt.grid()
plt.show()
