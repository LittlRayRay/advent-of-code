from collections import Counter

lines = open("input.txt", "r").read().splitlines()
lines = [line.split(" -> ") for line in lines]
init_string = "KOKHCCHNKKFHBKVVHNPN"
init_string = [char for char in init_string]
two_string = init_string[:]
print(lines)

for i in range(10):
    adj = 0
    for char in range(len(init_string)):
        for line in lines:
            try:
                if init_string[char] + init_string[char + 1] == line[0]:
                    two_string.insert(char + 1 + adj, line[1])
                    adj += 1 # to account for the insertion
            except:
                pass
    init_string = two_string[:]
print(two_string, init_string)

modal = max(init_string, key=init_string.count)
least = min(init_string, key=init_string.count)

modal_count = init_string.count(modal)
least_count = init_string.count(least)
print(modal_count - least_count)
print(modal_count, least_count)
print(modal, least)    
    