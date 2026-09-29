import sys
def func():
    l = sys.stdin.read().split()
    if not l:
        return
    times = int(l[1])
    word = l[2]
    for i in range(times):
        word = word.replace('BG', 'GB')
    print(word)

if __name__ == "__main__":
    func()