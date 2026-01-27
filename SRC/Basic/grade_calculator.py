def grade_calculator(marks_obtained):
    if 100 >= marks_obtained >= 90:
        print("Your Grade is: A")
    elif 89 >= marks_obtained >= 80:
        print("Your Grade is: B")
    elif 79 >= marks_obtained >= 70:
        print("Your Grade is: C")
    elif 69 >= marks_obtained >= 60:
        print("Your Grade is: D")
    elif 59 >= marks_obtained >= 0:
        print("Your Grade is: F")
    else:
        print("Wrong input")


grade_calculator(56)
grade_calculator(78)
grade_calculator(98)
grade_calculator(104)
