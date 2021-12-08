import time
start_time = time.time()
input = open("input7.txt", "r").read().split(",")
input.sort()
fuel_required, ntm = [], 994
for i in range(995):
    fuel_required.append(sum((abs(int(x) - i) for x in input)))
fuel_required.sort()
print(fuel_required[0])
print("Time taken: ", time.time() - start_time, " seconds!")