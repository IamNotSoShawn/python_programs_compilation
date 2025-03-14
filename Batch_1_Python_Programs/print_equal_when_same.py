def input_number (prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("please enter a valid input")
            
while True:
    num_1 = input_number ("enter the first number : ")
    num_2 = input_number ("enter the second number: ")

    if num_1==num_2:
        print("EQUAL")
    else:
        print("they are not equal")
        
    while True:
        loop = input("Do you want to try again?  type yes or no: ")
        if loop in ["yes"]:
            break
        elif loop in ["no"]:
            print("Goodbye !")
            exit()
        else:
            print("invalid")
