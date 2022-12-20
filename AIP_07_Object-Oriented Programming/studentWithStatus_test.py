import studentWithStatus

def main():
  name = input("Enter student's name:")
  midterm = float(input("Enter grade on midterm:"))
  final = float(input("Enter grade on final:"))
  category = input("Enter category (LG or PF):")

  if category.upper() == "LG":
    st = studentWithStatus.LGstudent(name, midterm, final)
  else:
    question = input("Is" + name + " a full time student (Y/N)?")

    if question.upper() == 'Y':
      fullTime = True
    else:
      fullTime = False

    st = studentWithStatus.PFstudent(name, midterm, final, fullTime)

  print("\nNAME\tGRADE\tSTATUS")
  print(st)


main()
