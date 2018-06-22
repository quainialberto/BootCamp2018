def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                                           "digits differ by 2 or more: ")
    if len(step_1) != 3:
        raise ValueError("You must input a 3-digit number")
    if abs(int(step_1[0]) - int(step_1[2])) < 2:
        raise ValueError("First and last digits must differ by 2 or more")
    step_2 = input("Enter the reverse of the first number, obtained "
                                              "by reading it backwards: ")
    if step_2 != step_1[::-1]:
        raise ValueError("The second number is not the reverse of the first number")
    step_3 = input("Enter the positive difference of these numbers: ")
    if int(step_3) != abs(int(step_1) - int(step_2)):
        raise ValueError("The third number is not the positive difference of the"
                " first two numbers")
    step_4 = input("Enter the reverse of the previous result: ")
    if step_4 != step_3[::-1]:
        raise ValueError("The forth number is not the reverse of the third number")

    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")

arithmagic()
