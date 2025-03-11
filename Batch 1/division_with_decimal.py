def func (prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter numbers only")

while True:
    num_1 = func("enter your first number: (this number will be the dividend): ")
    num_2 = func("enter your second number (this number will be the divisor): ")
    quo = num_1/num_2
    print(quo)
    
    while True:
        loop = input("do you want to try again? enter yes or no only: ")
        if loop in["yes"]:
            break
        elif loop in ["no"]:
            print("thankyou for using my program hehes :>")
            exit()
        else:
            print("type yes or no only !")