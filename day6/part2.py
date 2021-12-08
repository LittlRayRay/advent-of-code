lanternfish_list = open("input.txt", "r").read().split(",")

days = 0
zy = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7: 0, 8:0}

for l in lanternfish_list:
    zy[int(l)] += 1 

print(zy)

for i in range (256):
    i = {8:zy[0], 7:zy[8], 6:zy[7] + zy[0], 5:zy[6], 4:zy[5], 3:zy[4], 2:zy[3], 1:zy[2], 0:zy[1]}
    zy = i  

print(zy)
print(sum(zy.values()))
print(open("input.txt", "r").read())

