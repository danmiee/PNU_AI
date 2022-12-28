import random
import math

# 나중에 사용하기 위한 전역변수 선언
DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations


def main():
    # Create an instance of numerical optimization problem
    # 입력 txt 파일에서 수식과 변수의 범위를 읽어와 반환
    p = createProblem()   # 'p': (expr, domain)

    # Call the search algorithm
    # SteepestAscent 알고리즘을 실행하여 solution을 구하기
    solution, minimum = steepestAscent(p)

    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()

    # Report results
    displayResult(solution, minimum)


def createProblem():
    # Read in an expression and its domain from a file.

    # input function을 이용해 읽어올 txt 파일의 경로를 얻어옴
    fileName = input("파일명을 입력하세요.")
    infile = open(
        'AIP_09_SearchAlgorithms/Search_Tool_Sample_Problems/'+fileName, 'r')

    # 'expression' is a string.
    # 'expression'은 txt 파일의 첫 줄에 있는 수식 string
    # readline()을 이용해 각 줄의 정보를 읽어옴
    expression = infile.readline().rstrip()

    # 'varNames' is a list of variable names.
    varNames = []
    # 'low' is a list of lower bounds of the varaibles.
    low = []
    # 'up' is a list of upper bounds of the varaibles.
    up = []

    # line  = infile.readline().rstrip()
    # while line != '':
    for line in infile:
        # txt 파일의 두 번째 줄 부터는 변수명,최소값,최대값
        d = line.split(",")
        # 'varNames'는 각 변수의 이름이 저장 됨
        varNames.append(d[0])
        # 'low'에는 각 변수의 최소값이 저장됨
        low.append(eval(d[1]))
        # 'up'에는 각 변수의 최대값이 저장됨
        up.append(eval(d[2]))
        # while문 사용 시 다음 값 판단 위해 line 확인
        # line = f.readline().rstrip()

    # 'domain' is a list of 'varNames', 'low', and 'up'.
    domain = [varNames, low, up]
    infile.close()

    # Then, return a problem 'p'.
    # 'p' is a tuple of 'expression' and 'domain'.
    return expression, domain


def steepestAscent(p):
    # Random한 초기값을 생성
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while True:
        # mutant를 생성
        neighbors = mutants(current, p)
        # mutant 중 가장 좋은 solution을 선택
        successor, valueS = bestOf(neighbors, p)
        # best solution 업데이트
        # print('valueC:', valueC)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    
    # Best solution과 그때의 Cost를 반환

    return current, valueC


def randomInit(p):
    # Return a random initial point
    # as a list of values
    # 초기 값을 만들기 위해 랜덤한 값들을 만들기

    # domain의 low, up 정보를 이용해
    domain = p[1]
    low, up = domain[1], domain[2]
    # low <= value <= up 범위에 해당하는 값을 random.uniform을 통해 생성
    # list 형태로 각 변수의 초기 값을 반환
    # 랜덤한 숫자 만들어서 init.append하기
    init = []
    for i in range(len(low)):
        init.append(random.uniform(low[i], up[i]))
    return init


def evaluate(current, p):
    # Evaluate the expression of 'p' after assigning
    # the values of 'current' to the variables

    # Number of evaluation을 기록하기 위해 global 변수 이용
    global NumEval  # (원칙) NumEval이 글로벌임을 알려주기
    NumEval += 1

    # expression과 variable name을 읽어오고
    expression = p[0]
    domain = p[1]
    varNames = domain[0]  # 여기에서 변수명 참조

    for i in range(len(varNames)):
        # 이를 이용해 x=value 형태의 string을 만든 뒤,
        ## x1, x2, x3, x4, x5에 현재 값을 저장한 후
        ## 'x1=0.5'와 같은 형태로 string을 만들어 exec함수 이용
        ## 왜냐하면 'x1', 'x2'와 같은 변수명을 이미 저장해두었기 때문
        cmd = varNames[i] + '=' + str(current[i])
        # exec 를 이용해 실제로 실행하여 값을 할당 후
        ## exec('x1' + '=' + str(CURRENT_VALUE))
        ## eval : 값 반환 / exec : 값 할당, 반환x
        ## 결과적으로 x1에 CURRENT_VALUE가 할당됨
        exec(cmd)

    # expression을 eval하여 현재 함수값 계산
    valueC = eval(expression)
    
    # 함수를 current 값을 이용해서 계산한 값
    return valueC


def mutants(current, p):
    # Return a set of successors
    # mutate 함수를 사용해 +DELTA, -DELTA 두가지 경우에 대한 mutant 생성
    # 모든 변수에 대해 mutation 실시하여 list 형태로 저장하여 반환
    neighbors = []

    # 2번 인덱스의 변수가 DELTA만큼 바뀐 m 생성
    # m = mutate(current, 2, DELTA, p)

    # float은 소수점을 정확하게 나타낼 수 없기 때문에 끝자리가 변경될 수 있으나 무의미한 수치로 봄
    for i in range(len(current)):
        m = mutate(current, i, DELTA, p)
        neighbors.append(m)
        m = mutate(current, i, -DELTA, p)
        neighbors.append(m)

    return neighbors


def mutate(current, i, d, p):  # Mutate i-th of 'current' if legal
    # 현재 값에 대한 복사본을 slicing을 이용해 생성
    neighbor = current[:]

    # 복사 된 값에 mutation을 실시하며, 이 때 domain 정보를 이용해
    domain = p[1]
    low, up = domain[1], domain[2]

    # low <= value <= up 사이의 유효한 값이 얻어지도록 확인
    if low[i] <= neighbor[i] + d <= up[i]:
        neighbor[i] += d

    # neighbor : 값이 5개 들어있는 list (current와 동일한 형태)
    return neighbor


def bestOf(neighbors, p):
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환

    # 1. 가장 처음 sample을 best라고 가정
    best = neighbors[0]
    bestValue = evaluate(best, p)

    # 2. 두번째부터 계속 비교하며 더 좋은 게 찾아지면 best로 저장
    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue:
            bestValue = newValue

    # 3. 비교가 끝나면 best 반환
    return best, bestValue


def describeProblem(p):
    print()
    print("Objective function:")
    # expression 출력
    print(p[0])   # Expression
    print("Search space:")
    # Domain 정보 출력
    varNames = p[1][0]  # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i]))


def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)


def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))


def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
