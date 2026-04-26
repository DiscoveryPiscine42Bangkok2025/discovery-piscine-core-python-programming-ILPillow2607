import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    while len(text) < 8:
        text += "Z"
    print(text)

def main():
    if len(sys.argv) == 1:
        print("none")
        return
    
    param = sys.argv[1:]
    for p  in param:
        if len(p) > 8:
            shrink(p)
        elif len(p) < 8:
            enlarge(p)
        else:
            print(p)

if __name__ == "__main__":
    main()

#python methods_everywhere.py "lol" "physically" "backpack" (for try this code)
