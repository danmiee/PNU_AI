import random
import math

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


def createProblem(): ###
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'expression'은 txt 파일의 첫 줄에 있는 수식 string
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## txt 파일의 두 번째 줄 부터는 변수명,최소값,최대값
    ## 'varNames' is a list of variable names.
    ## 'varNames'는 각 변수의 이름이 저장 됨
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'low'에는 각 변수의 최소값이 저장됨
    ## 'up' is a list of upper bounds of the varaibles.
    ## 'up'에는 각 변수의 최대값이 저장됨

    # input function을 이용해 읽어올 txt 파일의 경로를 얻어옴
    # readline()을 이용해 각 줄의 정보를 읽어옴
    return expression, domain


def steepestAscent(p):
    # Random한 초기값을 생성
    
    # 초기값에 대한 함수값을 계산
    
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    
        # mutant를 생성
        
        # mutant 중 가장 좋은 solution을 선택
        
        # best solution 업데이트
        



    # Best solution과 그때의 Cost를 반환
    return current, valueC


def randomInit(p):
    # Return a random initial point
    # as a list of values
    # 초기 값을 만들기 위해 랜덤한 값들을 만들기

    # domain의 low, up 정보를 이용해
    # low <= value <= up 범위에 해당하는 값을 random.uniform을 통해 생성
    # list 형태로 각 변수의 초기 값을 반환

    return init    


def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables

    # Number of evaluation을 기록하기 위해 global 변수 이용
    

    # expression과 variable name을 읽어오고
    # 이를 이용해 x=value 형태의 string을 만든 뒤,
    # exec 를 이용해 실제로 실행하여 값을 할당 후
    # expression에 eval을 이용해 함수 값을 계산

    return


def mutants(current, p):
    # Return a set of successors
    # mutate 함수를 사용해 +DELTA, -DELTA 두가지 경우에 대한 mutant 생성
    # 모든 변수에 대해 mutation 실시하여 list 형태로 저장하여 반환

    return neighbors     


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    # 현재 값에대한 복사본을 slicing을 이용해 생성
    
    # 복사 된 값에 mutation을 실시하며, 이 때 domain 정보를 이용해
    # low <= value <= up 사이의 유효한 값이 얻어지도록 확인



    return

def bestOf(neighbors, p):
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환
    
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    # expression 출력
    print(p[0])   # Expression
    print("Search space:")
    # Domain 정보 출력
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
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
