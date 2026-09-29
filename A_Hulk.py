x = int(input())
l = []
for i in range(1, x+1):
    if i % 2 == 0:
        l.append("I love")
    else:
        l.append("I hate")

print(" that ".join(l) + " it ")