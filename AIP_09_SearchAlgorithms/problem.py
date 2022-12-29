import random
import math

class Problem:
    # 모든 클래스 메소드에 self가 붙는 이유
    # 내 자신에 대한 참조 - 예외 : static 메소드
    
    def __init__(self):
        self._solution = None
        self._value = 0         # Minimum
        self._numEval = 0

    def setVariables(self):
        pass  # 기능이 있어야하는데 상속받는 클래스에서 구현할 것임을 표현
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):
        super().__init__()
        self._expression = ''
        self._domain = []
        self._delta = 0.01
    
    def setVariables(self):
        # 입력파일을 input으로 받아서 createProblrm과 동일한 동작
        # 이후 self._expression, self._domain 업데이트
        fileName = input("파일명을 입력하세요.")
        infile = open('./Search_Tool_Sample_Problems/'+fileName, 'r')
        self._expression = infile.readline().rstrip()

        varNames = []
        low = []
        up = []

        for line in infile:
            d = line.split(",")
            varNames.append(d[0])
            low.append(eval(d[1]))
            up.append(eval(d[2]))
        self._domain = [varNames, low, up]
        infile.close()

    def getDelta(self):
        return self._delta
    
    def randomInit(self): # Return a random initial point as a list
        low, up = self._domain[1], self._domain[2]
        init = []
        for i in range(len(low)):
            init.append(random.uniform(low[i], up[i]))
        return init

    def evaluate(self, current):
        self._numEval += 1
        varNames = self._domain[0]
        for i in range(len(varNames)):
            cmd = varNames[i] + '=' + str(current[i])
            exec(cmd)
        valueC = eval(self._expression)
        return valueC
    
    def mutants(self, current):
        neighbors = []
        for i in range(len(current)):
            m = self.mutate(current, i, self._delta)
            neighbors.append(m)
            m = self.mutate(current, i, -self._delta)
            neighbors.append(m)
        return neighbors

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        neighbor = current[:]
        low, up = self._domain[1], self._domain[2]
        if low[i] <= neighbor[i] + d <= up[i]:
            neighbor[i] += d
        return neighbor

    def randomMutant(self, current):
        i = random.randint(0, len(current) - 1)
        if random.uniform(0, 1) > 0.5:
            d = self._delta
        else:
            d = -self._delta
        return self.mutate(current, i, d)

    def describe(self):
        print()
        print("Objective function:")
        # expression 출력
        print(self._expression)   # Expression
        print("Search space:")
        # Domain 정보 출력
        varNames = self._domain[0]  # self._domain is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def report(self):
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        super().report() 

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple

class Tsp(Problem):
    def __init__(self):
        super().__init__()
        self._numCities = 0
        self._locations = []
        self._distanceTable = []
        
    def setVariables(self):
        fileName = input("파일명을 입력하세요.")
        infile = open(
            './Search_Tool_Sample_Problems/'+fileName, 'r')
        self._numCities = int(infile.readline())
        self._locations = []
        line = infile.readline()
        while line != '':
            self._locations.append(eval(line))  # eval : string에서 tuple로 변환
            line = infile.readline()
        infile.close()
        self.calcDistanceTable()

    def calcDistanceTable(self):
        for i in range(self._numCities):
            row = []
            for j in range(self._numCities):
                dx = self._locations[i][0] - self._locations[j][0]
                dy = self._locations[i][1] - self._locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2), 1)
                row.append(d)
            self._distanceTable.append(row)

    def randomInit(self):
        init = list(range(self._numCities))
        random.shuffle(init)
        return init
    
    def evaluate(self, current):
        self._numEval += 1
        cost = 0
        for i in range(self._numCities-1):
            cost += self._distanceTable[current[i]][current[i+1]]
        return cost
    
    def mutants(self, current):
        neighbors = []
        triedPairs = []
        while len(neighbors) < self._numCities:
            i = random.randint(0, self._numCities-2)
            j = random.randint(i+1, self._numCities-1)
            if [i, j] in triedPairs:
                continue
            else:
                triedPairs.append([i, j])
            neighbors.append(self.inversion(current, i, j))
        return neighbors

    def inversion(self, current, i, j):
        curCopy = current[:]
        s = curCopy[i:j+1]
        s.reverse()
        curCopy[i:j+1] = s
        return curCopy

    def randomMutant(self, current):
        while True:
            i, j = sorted([random.randrange(self._numCities) for _ in range(2)])
            if i < j:
                mutant = self.inversion(current, i, j)
                break
        return mutant
    
    def describe(self):
        print()
        print("Number of cities:", self._numCities)
        print("City locations:")
        for i in range(self._numCities):
            print("{0:>12}".format(str(self._locations[i])), end='')
            if i % 5 == 4:
                print()

    def report(self):
        print()
        print("Best order of visits:")
        self.tenPerRow()       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._value)))
        super().report()

    def tenPerRow(self):
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()
