def input_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("use numbers only !")
            
            
while True:
    total = 0
    for count in range(1,11):
        while True:
            try:
                num = input_number("enter your number: ")
                total += num
                break
            except ValueError:
                print("use numbers only !")
    print(total)
    
    while True:
        loop = input ("type yes or no to loop: ")
        if loop in ["yes"]:
            break
        elif loop in ["no"]:
            print("thankyou for using my program !")
            exit()
        else:
            ("type yes or no only !")
            
