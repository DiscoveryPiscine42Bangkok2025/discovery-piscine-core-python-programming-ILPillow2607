import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    text = sys.argv[1]
    count = 0
    for char in text:
        if char == "z":
            count += 1
        
    if count == 0:
        print("none")
    else:
        print("z" * count)

if __name__ == "__main__":
    main()
#python string_are_arrays.py "Zaz visits the zoo with Zazie" (for try this code)
