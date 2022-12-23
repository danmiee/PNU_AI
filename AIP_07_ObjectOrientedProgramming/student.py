class Student:
  def __init__(self, name="", midterm=0, final=0):
    self._name = name
    self._midterm = midterm
    self._final = final

  def setName(self, name):
    self._name = name

  def setMidterm(self, midterm):
    self._midterm = midterm

  def setFinal(self, final):
    self._final = final

  def getName(self):
    return self._name

  def __str__(self):
    return self._name + "\t" + self.calcSemGrade()

# Student를 superclass로 갖는 LGstudent


class LGstudent(Student):
  # init, get, set 없지만 상속받았기에 사용 가능
  # Grade 계산 메소드 추가
  def calcSemGrade(self):
    average = round((self._midterm + self._final) / 2)
    if average >= 90:
      return "A"
    elif average >= 80:
      return "B"
    elif average >= 70:
      return "C"
    elif average >= 60:
      return "D"
    else:
      return "F"


class PFstudent(Student):
  # Polymorphism(다형성) : 같은 이름, 다른 형태
  def calcSemGrade(self):
    average = round((self._midterm + self._final) / 2)
    if average >= 60:
      return "Pass"
    else:
      return "Fail"
