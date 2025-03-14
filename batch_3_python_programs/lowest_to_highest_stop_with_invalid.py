user_numbers = []
while True:
    try:
        number = int(input("enter any number, enter an invalid input to stop like a letter or symbol: "))  
        user_numbers.append(number) 
    except ValueError:
        break  

if user_numbers:
    user_numbers.sort()  
    print("numbers from lowest to highest: ", user_numbers)
else:
    print("no numbers entered")
