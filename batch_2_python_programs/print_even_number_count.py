def input_num (prompt):
    while True:
        try: 
            num = float(input(prompt))
            return num
        except ValueError:
            print("enter numbers only")

even_number_count = 0
for count in range (1,11):
    while True:
        try:
            number = input_num("enter any number: ")
            if number%2 == 0:
                even_number_count +=1
            break
        except RuntimeError:
            print("Please restart the program")
print("This is how many even numbers you have entered: ",even_number_count)            
