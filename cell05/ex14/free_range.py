import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("none")
        return
    
    numbers = list(range(start, end + 1))
    print(numbers)

if __name__ == "__main__":
    main()
#python free_range.py 10 14 (for try this code)
