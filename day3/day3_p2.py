input = open('day3/input.txt', 'r').read().splitlines()
print(input)

zero_count, one_count = 0, 0 # zero_count, one_count, idx


zeroes_removed, ones_removed = 0,0

for idx in range(len(input[0])):

    test_input = []
    q = 1

    for i in input:
        if i[idx] == '0':
            zero_count += 1
        elif i[idx] == '1':
            one_count += 1
    
    if zero_count > one_count:
        print("remove 0")
        zeroes_removed += 1
        for line in input:
            if line[idx] == "1":
                test_input.append(line)
                
        
    elif zero_count <= one_count: 
        print("remove 1")
        ones_removed += 1
        for line in input:
            if line[idx] == "0":
                test_input.append(line)
                q += 1
                print(f"done!{q}")
                    
    input = test_input[:]

    test_input = []

    zero_count, one_count = 0, 0

        
            


print (input)
print(zeroes_removed, ones_removed)
