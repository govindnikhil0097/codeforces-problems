import sys
def func():
    l = sys.stdin.read().split()
    word = set(l[0])
    if not l:
        return

    if len(word) % 2 == 0:  
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == "__main__":
    func()