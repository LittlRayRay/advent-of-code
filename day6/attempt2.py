fls=open("input.txt", "r").read().split(",")

flsToAdd = fls

for x in range(256):
    index = 0

    for i in fls:
        if fls[index] == 0:
            flsToAdd[index] = 6
            flsToAdd.append(9)
        else:

            flsToAdd[index] = int(fls[index]) - 1
        index+=1 
    fls = flsToAdd
print(len(fls))

