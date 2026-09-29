import sys
def func():
    l = sys.stdin.read().split()
    if not l:
        return
    d = int(l[-1])
    k, l, m, n = int(l[0]), int(l[1]), int(l[2]), int(l[3])
    damage = 0
    for i in range(1, d+1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            damage += 1
    print(damage)

if __name__ == "__main__":
    func()