#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

def input_num (prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Enter numbers only !")

while True:
    num_1 = input_num("enter your first number: ")
    subtrahend = 0
    for count in range(1,10):
        while True:
            try:
                number = input_num("enter a numbers that will be subtracted to the first number: ")
                subtrahend += number
                break
            except ValueError:
                print("invalid input, enter numbers only")
                
    answer = num_1 - subtrahend 
    print(answer)
    
    while True:
        loop = input ("type yes or no to try again: ")
        if loop in ["yes"]:
            break
        elif loop in ["no"]:
            print("thankyou for using my program")
            exit()
        else:
            print("invalid input, enter yes or no only")
        