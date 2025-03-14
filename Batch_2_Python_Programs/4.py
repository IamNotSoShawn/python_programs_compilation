def input_num (prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Please enter numbers only")

while True:
    num_1 = input_num ("enter your first number: (this number will be the dividend): ")
    num_2 = input_num ("enter your second number (this number will be the divisor): ")
    quotient = num_1//num_2 
    print("The quotient without the decimal point is: ",quotient)
    
    while True:
        loop = input("do you want to try again? enter yes or no only: ")
        if loop in["yes"]:
            break
        elif loop in ["no"]:
            print("thankyou for using my program hehes :>")
            exit()
        else:
            print("type yes or no only !")