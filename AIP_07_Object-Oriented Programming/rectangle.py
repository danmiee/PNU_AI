class Rectangle:
    # 생성자
    def __init__(self, width=1, height=1):
        self._width = width
        self._height = height

    # mutator 메소드
    def setWidth(self, width):
        self._width = width

    def setHeight(self, height):
        self._height = height

    # 접근 메소드
    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2*(self._width + self._height)

    # 출력함수
    def __str__(self):
        return ("Width:"+str(self._width)+"\nHeight:"+str(self._height))
