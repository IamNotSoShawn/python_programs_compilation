lowest_num = None
while True:
    try:
        number = int(input("enter any number, enter an invalid input to stop like a letter or symbol: ")) 
        if lowest_num == None or number < lowest_num:
            lowest_num = number
    except ValueError:
        break 

if lowest_num != None:
    print("lowest number is :", lowest_num)
else:
    print("no numbers entered")
