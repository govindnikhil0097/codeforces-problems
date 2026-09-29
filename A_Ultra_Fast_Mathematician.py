#concept : comparing each element side by side

import sys
def func():
    l = sys.stdin.read().split()
    if not l:
        return
    n1 = l[0]
    n2 = l[1]
    string = ""
    for i, j in zip(n1, n2):
        if i == j:
            string += "0"
        else:
            string += "1"
    print(string)

if __name__ == "__main__":
    func()