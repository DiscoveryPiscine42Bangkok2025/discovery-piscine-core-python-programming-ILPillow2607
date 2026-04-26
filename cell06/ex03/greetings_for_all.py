def greetings(name ="noble stranger"):
    if not isinstance(name, str):
        print("Error, it was not a name.")
    else:
        print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
