input_num = []

while True:
    try:
        number = float(input("enter any number, enter an invalid input to stop like a letter or symbol: "))  
        if number in input_num:
            print("Duplicate")
        else:
            print("Unique")
            input_num.append(number) 
    except ValueError:
        print("thankyou for using my program !")
        break  
