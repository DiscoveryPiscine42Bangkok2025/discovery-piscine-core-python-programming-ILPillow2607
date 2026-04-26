import sys
def downcase_all(text):
    return text.lower()

def main():
    if len(sys.argv) == 1:
        print("none")
        return
    param = sys.argv[1:]
    for p in param:
        print(downcase_all(p))

if __name__ == "__main__":
    main()
#python downcase_all.py "HELLO WORLD" "I understood Arrays well!" (for try this code)
