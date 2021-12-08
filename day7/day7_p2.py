import time
start_time = time.time()
input = open("input7.txt", "r").read().split(",")
input.sort()
fuel_required, ntm = [], 994
total = 0
for i in range(995):
    total = 0
    for x in input:
        total_to_add = 0
        temp = abs(int(x) - i)
        total += temp * (temp + 1) / 2
    fuel_required.append(total)
    # fuel_required.append (sum((abs(int(x) - i) for x in input)*((abs(int(x) - i) for x in input)+1) / 2))
fuel_required.sort()
print(fuel_required[0])
print("Time taken: ", time.time() - start_time, " seconds!")
