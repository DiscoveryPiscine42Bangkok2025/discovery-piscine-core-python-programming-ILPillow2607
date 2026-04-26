def main():
    num = int(input("Enter a number less than 25\n"))

    if num > 25:
        print("Error")
        return

    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1  

if __name__ == "__main__":
    main()
