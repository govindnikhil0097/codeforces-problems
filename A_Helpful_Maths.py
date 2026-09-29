import sys

def func():
    l= sys.stdin.read().split()
    if not l:
        return
    string = l[0]
    numbers = []
    for i in string:
        for j in i:  
            if j in ['3', '2', '1']:
                numbers.append(j)
    numbers.sort()
    print("+".join(numbers))
if __name__ == "__main__":
    func()