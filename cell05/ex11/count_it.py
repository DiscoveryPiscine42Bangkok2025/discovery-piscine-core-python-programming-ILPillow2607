import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return
    
    param = sys.argv[1:]
    print(f"parameters: {len(param)}")

    for p in param:
        print(f"{p}: {len(p)}")

if __name__ == "__main__":
    main()

#python count_it.py "Game" "of" "Thrones" (for try this code)
