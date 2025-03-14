#blocks of codes to be reused for faster coding

                # function to enter numbers that has no restriction
def func (prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("please enter a numerical character")


                # function to enter numbers that can't have a negative input
def func (prompt):
    while True:
        try:
            num = float(input(prompt))
            if num < 0:
                print("number cant be negative")
                continue
            elif num == -0:
                print("negative 0 does not exist")
            return num
        except ValueError:
            print("please enter a numerical character")


                #while loop a entire code
while True:
# entire main code
    while True:
        loop = input ("type yes or no to loop: ")
        if loop in ["yes"]:
            break
        elif loop in ["no"]:
            print("thankyou for using my program !")
            exit()
        else:
            print("type yes or no only !")