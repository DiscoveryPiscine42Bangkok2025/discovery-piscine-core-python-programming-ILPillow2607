First_number = int(input("Enter the first number: "))
Second_number = int(input("Enter the second number: "))
mult = First_number * Second_number
print(First_number, "*", Second_number, "=", mult)
if mult == 0:
    print("The result is positive and negative.")
elif mult > 0:
    print("The result is positive.")
else:
    print("The result is negative.")
