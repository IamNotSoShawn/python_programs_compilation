def input_number (prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter numbers only")

while True:
    num_1 = input_number("enter your first number: (number to be raised)")
    num_2 = input_number("enter your second number (number to use as the power to raise the first): ")
    answer = num_1**num_2
    print(answer)
    
    while True:
        loop = input("do you want to try again? enter yes or no only: ")
        if loop in["yes"]:
            break
        elif loop in ["no"]:
            print("thankyou for using my program hehes :>")
            exit()
        else:
            print("type yes or no only !")