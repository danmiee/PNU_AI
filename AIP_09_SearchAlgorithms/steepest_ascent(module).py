from problem import Numeric


def main():
    # Numeric class instance 생성
    cls_num = Numeric()
    # setVariables를 이용해 문제 읽어오기
    cls_num.setVariables()
    # steepestAscent 실행
    steepestAscent(cls_num)
    # describe, report 이용해 결과 출력
    cls_num.describe()
    cls_num.report()


def steepestAscent(cls_num):
    current = cls_num.randomInit()
    valueC = cls_num.evaluate(current)
    while True:
        neighbors = cls_num.mutants(current)
        best, bestValue = bestOf(neighbors, cls_num)
        if bestValue < valueC:
            current = best
            valueC = bestValue
        else:
            break
    cls_num.storeResult(current, valueC)


def bestOf(neighbors, cls_num):
    best = neighbors[0]
    bestValue = cls_num.evaluate(best)

    for i in range(1, len(neighbors)):
        newValue = cls_num.evaluate(neighbors[i])
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue


def displaySetting(cls_num):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", cls_num.getDelta())


main()
