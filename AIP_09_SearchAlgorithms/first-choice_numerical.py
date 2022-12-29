import random
from problem import Numeric

# 나중에 사용하기 위한 전역변수 선언
LIMIT_STUCK = 10000

def main():
    cls_num = Numeric()
    # setVariables를 이용해 문제 읽어오기
    cls_num.setVariables()
    # steepestAscent 실행
    firstChoice(cls_num)
    # describe, report 이용해 결과 출력
    cls_num.describe()
    cls_num.report()


def firstChoice(cls_num):
    current = cls_num.randomInit()
    valueC = cls_num.evaluate(current)

    i = 0
    while i < LIMIT_STUCK:
        successor = cls_num.randomMutant(current)
        valueS = cls_num.evaluate(current)

        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    cls_num.storeResult(current, valueC)


def displaySetting(cls_num):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", cls_num.getDelta)


main()
