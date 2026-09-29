x = int(input())
y = 0
for i in range(x):
    w = input()
    if '+' in w:
        y += 1
    else:
        y -= 1
print(y)