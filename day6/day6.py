fls= open("input.txt", "r").read().split(",")
flsToAdd = []
index = 0
for i in range(80):
    flsToAdd = []
    for fish in fls:
        if fish == 0: 
            flsToAdd.append(8)
            fish = 6
        else: 
            fish -= 1
        index += 1

    fls.append(flsToAdd)
print(len(fls))
