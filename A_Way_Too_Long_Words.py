x = int(input())
for i in range(x):
    word = input()
    if len(word) > 10:
        first = word[0]
        last = word[-1]
        others = [str(x) for others in word[1:-1]]
        print(first + str(len(others)) + last)
    else:
        print(word)
