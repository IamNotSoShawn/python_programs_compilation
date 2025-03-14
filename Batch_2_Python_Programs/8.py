letsprint = input("type yes or no to print odd numbers from 0 to 100 using while loop: ")
if letsprint in ["no"]:
    print("Okay byeee")
    exit()
elif letsprint in ["yes"]:
    number = 1
    while number <= 100:
        print(number)
        number += 2
else:
    print("Invalid input, type yes or no only !")
