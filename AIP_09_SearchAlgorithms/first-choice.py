import random
import math

# 나중에 사용하기 위한 전역변수 선언
DELTA = 0.01   # Mutation step size
LIMIT_STUCK = 100
NumEval = 0    # Total number of evaluations


def main():
    p = createProblem()   # 'p': (expr, domain)
    solution, minimum = firstChoice(p)
    describeProblem(p)
    displaySetting()
    displayResult(solution, minimum)

def createProblem():
    fileName = input("파일명을 입력하세요.")
    infile = open(
        'AIP_09_SearchAlgorithms/Search_Tool_Sample_Problems/'+fileName, 'r')
    expression = infile.readline().rstrip()

    varNames = []
    low = []
    up = []

    line  = infile.readline().rstrip()
    while line != '':
        d = line.split(",")
        varNames.append(d[0])
        low.append(eval(d[1]))
        up.append(eval(d[2]))
        line = infile.readline().rstrip()

    domain = [varNames, low, up]
    infile.close()

    return expression, domain

def firstChoice(p):
    current = randomInit(p)
    valueC = evaluate(current, p)

    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(current, p)

        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    return current, valueC

def randomInit(p):

    domain = p[1]
    low, up = domain[1], domain[2]

    init = []
    for i in range(len(low)):
        init.append(random.uniform(low[i], up[i]))
    return init

def evaluate(current, p):
    global NumEval  # (원칙) NumEval이 글로벌임을 알려주기
    NumEval += 1

    expression = p[0]
    domain = p[1]
    varNames = domain[0]  # 여기에서 변수명 참조

    for i in range(len(varNames)):
        cmd = varNames[i] + '=' + str(current[i])
        exec(cmd)

    valueC = eval(expression)
    
    return valueC

def randomMutant(current, p):

    i = random.randint(0, len(current) - 1)
    if random.uniform(0, 1) > 0.5:
        d = DELTA
    else:
        d = -DELTA
    return mutate(current, i, d, p)

def mutate(current, i, d, p):  # Mutate i-th of 'current' if legal
    neighbor = current[:]
    domain = p[1]
    low, up = domain[1], domain[2]

    if low[i] <= neighbor[i] + d <= up[i]:
        neighbor[i] += d
    else:
        neighbor[i] = neighbor[i]

    return neighbor

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
