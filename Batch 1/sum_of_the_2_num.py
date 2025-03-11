def input_number (prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("enter numbers only")
while True:      
    num_1 = input_number("Enter first number: ")
    num_2 = input_number("Enter second number: ")
    sum = num_1+num_2
    print(sum)
    
    while True:
        again = input("Do you want to try another input? type yes or no: ")
        if again in ["yes"]:
            break
        elif again in ["no"]:
            print("thankyou for using my program, goodbye !")
            exit()
        else:
            print("type yes or no only")