import lgStudent


def main():
    listOfStudents = []
    carryOn = 'Y'

    while carryOn == 'Y':
        st = lgStudent.LGstudent()

        name = input("Enter student's name:")
        midterm = float(input("Enter grade on midterm exam:"))
        final = float(input("Enter grade on final exam:"))

        st = lgStudent.LGstudent(name, midterm, final)
        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)?")
        carryOn = carryOn.upper()

    print("\nNAME\tGRADE")

    for pupil in listOfStudents:
        print(pupil)


main()
