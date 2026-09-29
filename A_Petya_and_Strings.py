import sys
def func():
    l = sys.stdin.read().split()
    if not l:
        return
    w1 = l[0].lower()
    w2 = l[1].lower()
    if w1 == w2:
        print(0)
    elif w1 > w2:
        print(1)
    else:
        print(-1)

if __name__ == "__main__":
    func()