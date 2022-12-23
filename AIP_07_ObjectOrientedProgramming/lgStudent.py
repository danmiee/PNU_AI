def main():
    name = input("Enter student's name:")
    midterm = float(input("Enter grade on midterm exam:"))
    final = float(input("Enter grade on final exam:"))
    st = LGstudent(name, midterm, final)
    print("\nNAME\tGRADE")
    print(st)


class LGstudent:
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

    def calcSemGrade(self):
        grade = (self._midterm + self._final) / 2
        grade = round(grade)

        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "E"

    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()


main()
