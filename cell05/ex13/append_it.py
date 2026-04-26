import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return
    
    param = sys.argv[1:]
    printed = False
    for p in param:
        if not p.endswith("ism"):
            print(p + "ism")
            printed = True
    
    if not printed:
        print("none")

if __name__ == "__main__":
    main()
#python append_it.py "parallel" "egoism" "human" (for try this code)
