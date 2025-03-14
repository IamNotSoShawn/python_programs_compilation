def input_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("use numbers only !")
            
            
            
while True:
    odd = 0
    for count in range(1,11):
        while True:
            try:
                num = input_number("enter your number: ")
                if num%2 != 0:
                    odd += 1
                break
            except ValueError:
                print("use numbers only !")
    print(odd)
    
    while True:
        loop = input ("type yes or no to loop: ")
        if loop in ["yes"]:
            break
        elif loop in ["no"]:
            print("thankyou for using my program !")
            exit()
        else:
            print("Thankyou for using my program !")
            
