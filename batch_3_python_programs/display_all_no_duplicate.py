numbers = []
print("Enter 10 numbers:")

for inputs in range(10):
    while True:
        try:
            num = float(input("Enter a number: "))
            numbers.append(num)
            break
        except ValueError:
            print("Enter numbers only !")

special = []
for num in numbers:
    if numbers.count(num) == 1:  
        special.append(num)

if special:
    print("the numbers that don't have duplicates: ", special)
else:
    print("all numbers have duplicates")
