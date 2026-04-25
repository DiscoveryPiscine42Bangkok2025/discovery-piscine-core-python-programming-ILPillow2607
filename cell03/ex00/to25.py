number = int(input("Enter a number less than 25 : "))
if number < 25:
    print(number)
    for i in range(number, 26):
        print(i)
else:
    print("Error")
