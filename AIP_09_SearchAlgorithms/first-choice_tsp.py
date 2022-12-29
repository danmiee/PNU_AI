from problem import Tsp

# 나중에 사용하기 위한 전역변수 선언
LIMIT_STUCK = 10000


def main():
    cls_tsp = Tsp()
    # setVariables를 이용해 문제 읽어오기
    cls_tsp.setVariables()
    # steepestAscent 실행
    firstChoice(cls_tsp)
    # describe, report 이용해 결과 출력
    cls_tsp.describe()
    cls_tsp.report()


def firstChoice(cls_tsp):
    current = cls_tsp.randomInit()
    valueC = cls_tsp.evaluate(current)

    i = 0
    while i < LIMIT_STUCK:
        successor = cls_tsp.randomMutant(current)
        valueS = cls_tsp.evaluate(current)

        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    cls_tsp.storeResult(current, valueC)


def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print("Max evaluations with no improvement: {0:,} iterations".format(LIMIT_STUCK))


main()
