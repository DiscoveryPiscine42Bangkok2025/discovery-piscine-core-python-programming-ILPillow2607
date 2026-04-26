def add_one(x):
    x = x + 1

num = 5
print("Before:", num)
add_one(num)
print("After:", num)

#What do you observe?
#The value of num does not change because the add_one function does not store a value when called, 
#and the print command prints num, so it returns the same value.
#To get a new value, store the value in a new variable when calling the add_one function,
#then print the new variable.
