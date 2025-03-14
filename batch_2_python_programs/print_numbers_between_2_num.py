def input_num (prompt):
    while True:
        try: 
            num = int(input(prompt))
            return num
        except ValueError:
            print("enter numbers only")

num_1 = input_num("enter your first number: ")
num_2 = input_num("enter your second number: ")
if num_1 - num_2 == 1:
    print("numbers are close to each other")
elif num_2 - num_1 == 1:
    print("numbers are close to each other")
else:
    while num_1<num_2:
        num_1 += 1
        if num_1 == num_2:
            break
        print(num_1)
    while num_1>num_2:
        num_2 += 1
        if num_1 == num_2:
            break
        print(num_2)