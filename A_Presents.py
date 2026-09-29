import sys
def func():
    l = sys.stdin.read().split()
    if not l:
        return
    cases = int(l[0])
    gaveTo = [int(x) for x in l[1:]]
    gotBy = []
    for i in range(1, len(gaveTo)+1):  
        giver = gaveTo.index(i) + 1
        gotBy.append(str(giver))
    print(" ".join(gotBy))
        

if __name__ == "__main__":
    func()