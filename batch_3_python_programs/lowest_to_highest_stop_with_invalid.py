input_num = []
while True:
    try:
        number = int(input("enter any number, enter an invalid input to stop like a letter or symbol: "))  
        input_num.append(number) 
    except ValueError:
        break  

if input_num:
    input_num.sort()  
    print("numbers from lowest to highest: ", input_num)
else:
    print("no numbers entered")
